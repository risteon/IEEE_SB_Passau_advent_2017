cmake_minimum_required (VERSION 3.0)
project (ieee_advent_17)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

set(USE_DEBUG ON)
if (USE_DEBUG)
    set(CMAKE_BUILD_TYPE "Debug")
else()
    set(CMAKE_BUILD_TYPE "Release")
endif()

add_executable (06_pressure_in_the_printing_press 06_pressure_in_the_printing_press.cc)



