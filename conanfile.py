#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os

class TaskFlowConan(ConanFile):
    name = "cpp-taskflow"
    version = "2.2.0"
    description = "A Modern C++ Parallel Task Programming Library https://cpp-taskflow.github.io"
    topics = ("conan","taskflow")
    url = "https://github.com/zinnion/conan-cpp-taskflow"
    homepage = "https://github.com/cpp-taskflow/cpp-taskflow"
    author = "Zinnion <mauro@zinnion.com>"
    license = "MIT"
    exports = ["LICENSE.md"]
    exports_sources = ["CMakeLists.txt"]
    settings = "os", "compiler", "build_type", "arch"
    short_paths = True
    generators = "cmake"
    source_subfolder = "source_subfolder"
    build_subfolder = "build_subfolder"

    def source(self):
        tools.get("{0}/archive/v{1}.tar.gz".format(self.homepage, self.version))
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self.source_subfolder)

    def configure_cmake(self):
        cmake = CMake(self)
        cmake.configure(source_folder=self.source_subfolder, build_folder=self.build_subfolder)
        return cmake

    def build(self):
        cmake = self.configure_cmake()
        cmake.build()

    def package(self):
        cmake = self.configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
        self.cpp_info.libs.append('pthread')
