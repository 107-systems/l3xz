#######################################################################################
cmake_minimum_required(VERSION 3.8)
#######################################################################################
project(l3xz)
set(L3XZ_TARGET ${PROJECT_NAME})
#######################################################################################
if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()
#######################################################################################
find_package(ament_cmake REQUIRED)
#######################################################################################
add_library(${L3XZ_TARGET} STATIC
        src/types/HydraulicJoint.cpp
        src/types/Joint.cpp
        src/types/Leg.cpp
        )
#######################################################################################
target_include_directories(${L3XZ_TARGET} PRIVATE include)
#######################################################################################
target_compile_features(${L3XZ_TARGET} PRIVATE cxx_std_17)
#######################################################################################
ament_target_dependencies(${L3XZ_TARGET} ${THIS_PACKAGE_INCLUDE_DEPENDS})
#######################################################################################
ament_export_targets(${L3XZ_TARGET}_export HAS_LIBRARY_TARGET)
ament_export_dependencies(${THIS_PACKAGE_INCLUDE_DEPENDS})
#######################################################################################
install(DIRECTORY include/
        DESTINATION include
        )
install(TARGETS ${L3XZ_TARGET}
        EXPORT ${L3XZ_TARGET}_export
        LIBRARY DESTINATION lib
        ARCHIVE DESTINATION lib
        RUNTIME DESTINATION bin
        INCLUDES DESTINATION include
        )
install(DIRECTORY launch
        DESTINATION share/${PROJECT_NAME}
        )
#######################################################################################
ament_package()
#######################################################################################
