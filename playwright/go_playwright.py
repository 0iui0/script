from playwright.sync_api import Playwright, sync_playwright, expect  
import csv  
import os  
  
def extract_text(locator):  
    try:  
        return locator.text_content().strip()  
    except Exception as e:  
        print(f"Error extracting text: {e}")  
        return ""  
  
def run(url: str, page) -> None:  
    try:  
        page.goto(url)  
  
        # 等待表格数据加载完成  
        page.wait_for_selector("#resultDataRow1", timeout=2000)  
  
        # resultsCount
        count = page.locator(".resultsCount").text_content()
        # print("resultsCount: ", count)
        if count == "":
            with open('result.csv', 'a', newline='') as file:  
                writer = csv.writer(file)  
                writer.writerow([", ".join("0"), 0, 0, 0, 0, 0])
            return
        if count != "1":
            with open('result.csv', 'a', newline='') as file:  
                writer = csv.writer(file)  
                writer.writerow([", ".join("#"), count, count, count, count, count])
            return
        # 提取表格数据  
        table_row = page.locator("#resultDataRow1")  
        author_names = [div.text_content().strip().replace('\n', ' ') for div in table_row.locator(".authorResultsNamesCol").element_handles()]  
        documents_count = extract_text(table_row.locator("#resultsDocumentsCol1"))  
        h_index = extract_text(table_row.locator(".dataCol4"))  
        affiliation = extract_text(table_row.locator(".dataCol5"))  
        city = extract_text(table_row.locator(".dataCol6"))  
        country = extract_text(table_row.locator(".dataCol7"))  
  
        # 打印输出所有数据  
        # print(author_names, documents_count, h_index, affiliation, city, country)  
  
        # 将数据保存到CSV文件  
        with open('result.csv', 'a', newline='') as file:  
            writer = csv.writer(file)  
            writer.writerow([", ".join(author_names), documents_count, h_index, affiliation, city, country])  
  
    except Exception as e:
        with open('result.csv', 'a', newline='') as file:  
            writer = csv.writer(file)  
            writer.writerow([", ".join("e"), 0, 0, 0, 0, 0])  
        # print(f"An error occurred: {e}")

if __name__ == "__main__":  
    # 打印表头  
    print("作者,文献,h-index,归属机构,城市,国家/地区")  
    # 检查文件是否为空，如果为空则写入表头  
    if not os.path.exists('result.csv') or os.path.getsize('result.csv') == 0:  
        with open('result.csv', 'w', newline='', encoding='utf-8') as file:  
            writer = csv.writer(file)  
            writer.writerow(["作者", "文献", "h-index", "归属机构", "城市", "国家/地区"])  
  
    with sync_playwright() as playwright:  
        browser = playwright.chromium.launch(headless=False)  
        context = browser.new_context()  
        page = context.new_page()  
  
        # 读取link.csv中的URL列表  
        try:  
            with open('link.csv', 'r', encoding='utf-8') as file:  
                urls = [line.strip() for line in file if line.strip()]  
        except Exception as e:  
            print(f"Error reading links from link.csv: {e}")  
            browser.close()  
            exit(1)  
  
        # 使用Playwright处理每个URL  
        for url in urls:  
            try:  
                run(url, page)  
            except Exception as e:  
                print(f"Error processing URL {url}: {e}")  
  
        context.close()  
        browser.close()