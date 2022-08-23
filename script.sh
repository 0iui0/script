/opt/clion/bin/cmake/linux/bin/cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_C_COMPILER=/opt/android/sdk/ndk/22.1.7171670/toolchains/llvm/prebuilt/linux-x86_64/bin/aarch64-linux-android30-clang -DCMAKE_CXX_COMPILER=/opt/android/sdk/ndk/22.1.7171670/toolchains/llvm/prebuilt/linux-x86_64/bin/aarch64-linux-android30-clang++ -DCMAKE_TOOLCHAIN_FILE=/opt/android/sdk/ndk/22.1.7171670/build/cmake/android.toolchain.cmake -DANDROID_NDK=/opt/android/sdk/ndk/22.1.7171670 -DANDROID_ABI=arm64-v8a -DANDROID_PLATFORM=android-30 -DANDROID_STL=c++_shared -G "CodeBlocks - Unix Makefiles" ..

boost:

/opt/clion-2022.1.3/bin/cmake/linux/bin/cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_C_COMPILER=/opt/android/sdk/ndk/25.0.8775105/toolchains/llvm/prebuilt/linux-x86_64/bin/aarch64-linux-android30-clang -DCMAKE_CXX_COMPILER=/opt/android/sdk/ndk/25.0.8775105/toolchains/llvm/prebuilt/linux-x86_64/bin/aarch64-linux-android30-clang++ -DCMAKE_TOOLCHAIN_FILE=/opt/android/sdk/ndk/25.0.8775105/build/cmake/android.toolchain.cmake -DANDROID_NDK=/opt/android/sdk/ndk/22.1.7171670 -DANDROID_ABI=arm64-v8a -DANDROID_PLATFORM=android-30 -DANDROID_STL=c++_shared -DEIGEN3_INCLUDE_DIR=/usr/include/eigen3  -G "CodeBlocks - Unix Makefiles" -DANDROID=ON ..


gtsam:

 /opt/clion-2022.1.3/bin/cmake/linux/bin/cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_C_COMPILER=/opt/android/sdk/ndk/25.0.8775105/toolchains/llvm/prebuilt/linux-x86_64/bin/aarch64-linux-android30-clang -DCMAKE_CXX_COMPILER=/opt/android/sdk/ndk/25.0.8775105/toolchains/llvm/prebuilt/linux-x86_64/bin/aarch64-linux-android30-clang++ -DCMAKE_TOOLCHAIN_FILE=/opt/android/sdk/ndk/25.0.8775105/build/cmake/android.toolchain.cmake -DANDROID_NDK=/opt/android/sdk/ndk/25.0.8775105 -DANDROID_ABI=arm64-v8a -DANDROID_PLATFORM=android-30 -DANDROID_STL=c++_shared    -G "CodeBlocks - Unix Makefiles" -DEIGEN3_INCLUDE_DIR=/usr/include/eigen3

set(Boost_DEBUG 1)
set(Boost_COMPILER "-clang")
set(BOOST_LIB_PREFIX "lib")
set(Boost_LIB_PREFIX "-a64")
set(BOOST_ROOT ~/Boost-for-Android/build/out/arm64-v8a)
set(Boost_INCLUDE_DIR ~/Boost-for-Android/build/out/arm64-v8a/include/boost-1_74)
set(BOOST_LIBRARYDIR ~/Boost-for-Android/build/out/arm64-v8a/lib)
set(Boost_SERIALIZATION_LIBRARY ${BOOST_LIBRARYDIR}/libboost_serialization-clang-mt-a64-1_74.a)
set(Boost_SYSTEM_LIBRARY ${BOOST_LIBRARYDIR}/libboost_system-clang-mt-a64-1_74.a)
set(Boost_FILESYSTEM_LIBRARY ${BOOST_LIBRARYDIR}/libboost_filesystem-clang-mt-a64-1_74.a)
set(Boost_THREAD_LIBRARY ${BOOST_LIBRARYDIR}/libboost_thread-clang-mt-a64-1_74.a)
set(Boost_DATE_TIME_LIBRARY ${BOOST_LIBRARYDIR}/libboost_date_time-clang-mt-a64-1_74.a)


