#!/bin/sh
# Bootstrap gradlewrapper.jar without gradle
# (C) 2022 OpenMandriva Association https://openmandriva.org/
# Released under the GPLv3

rm -rf gradlewrapper-src
cp -a subprojects/wrapper/src/main/java gradlewrapper-src
cp -a subprojects/cli/src/main/java/org gradlewrapper-src
cp -a subprojects/wrapper-shared/src/main/java/org gradlewrapper-src
cd gradlewrapper-src
find . -name "*.java" |xargs javac
mkdir META-INF
cat >META-INF/MANIFEST.MF <<EOF
Manifest-Version: 1.0
Implementation-Title: Gradle Wrapper
Main-Class: org.gradle.wrapper.GradleWrapperMain
EOF
find . -name "*.class" |xargs jar -c -v -m META-INF/MANIFEST.MF -f gradle-wrapper.jar META-INF
