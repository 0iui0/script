from playwright.sync_api import Playwright, sync_playwright, expect  
import csv  
import os

def run(url: str, page) -> None:
    page.goto(url)

    # 等待表格数据加载完成，这里需要根据实际情况调整选择器, 目前假设只有一个表格，返回一条结果。等待5秒，超时则返回
    try:
        page.wait_for_selector("#resultDataRow1", timeout=5000)  # Timeout in milliseconds
    except:
        print("Timeout occurred while waiting for selector")
        return 
    
    # 提取表格数据  
    table_row = page.locator("#resultDataRow1")  
    # 作者
    author_cell = table_row.locator(".authorResultsNamesCol")
    author_names = [div.text_content().strip().replace('\n', ' ') for div in table_row.locator(".authorResultsNamesCol").element_handles()]  
    # 注意：这里的选择器需要根据实际的HTML结构进行调整， 这里不记录序号了
    documents_count = table_row.locator("#resultsDocumentsCol1").text_content().strip()
    # h-index
    h_index = table_row.locator(".dataCol4").text_content().strip()
    # 归属机构
    affiliation = table_row.locator(".dataCol5").text_content().strip()
    # 城市
    city = table_row.locator(".dataCol6").text_content().strip()
    # 国家
    country = table_row.locator(".dataCol7").text_content().strip()

    # 打印输出所有数据
    print(author_names, documents_count, h_index, affiliation, city, country)
    # 将数据保存到CSV文件  
    with open('result.csv', 'a', newline='') as file:  # 使用'a'模式以追加数据  
        writer = csv.writer(file)  
        writer.writerow([", ".join(author_names), documents_count, h_index, affiliation, city, country])  

  
# 主程序入口  
if __name__ == "__main__":  
    # 打印表头
    print("作者,文献,h-index,归属机构,城市,国家/地区")
    # 检查文件是否为空，如果为空则写入表头  
    if not os.path.exists('result.csv') or os.path.getsize('result.csv') == 0:  
        with open('result.csv', 'w', newline='') as file:  
            writer = csv.writer(file)  
            writer.writerow(["作者", "文献", "h-index", "归属机构", "城市", "国家/地区"])  

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # 读取link.csv中的URL列表  
        with open('link.csv', 'r') as file:
            urls = [line.strip() for line in file]
        
        # 使用Playwright处理每个URL  
        for url in urls:
            run(url, page)

        context.close() 