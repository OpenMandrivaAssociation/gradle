# Built from source. The bootstrap compiler is gradle-bootstrap 8.11.1.
# native-platform and gradle-fileevents are embedded in the distribution,
# so this package is built for each architecture.

%global __jar_repack 0
%global __provides_exclude_from .*
%global __requires_exclude_from .*
%global __noautoreq '^.*$'
%global __noautoprov '^.*$'
# Natives are embedded inside the distribution jars.
%global debug_package %{nil}

Name:		gradle
Version:	9.9.2
Release:	1
Summary:	The Gradle build tool
License:	Apache 2.0
URL:		https://gradle.org/
Group:		Development/Tools

Source0:	gradle-%{version}-src.tar.gz
Source1:	gradle-bootstrap-tools.tar.gz
Patch0:		gradle-%{version}-bootstrap.patch

BuildRequires:	angus-activation
BuildRequires:	animal-sniffer-annotations
BuildRequires:	ant-lib
BuildRequires:	antlr-runtime
BuildRequires:	antlr-tool
BuildRequires:	antlr4
BuildRequires:	antlr4-tool
BuildRequires:	aopalliance
BuildRequires:	apache-commons-bcel
BuildRequires:	apache-commons-cli
BuildRequires:	apache-commons-codec
BuildRequires:	apache-commons-collections4
BuildRequires:	apache-commons-compress
BuildRequires:	apache-commons-csv
BuildRequires:	apache-commons-io
BuildRequires:	apache-commons-lang3
BuildRequires:	apache-commons-logging
BuildRequires:	apache-commons-net
BuildRequires:	apache-commons-parent
BuildRequires:	apache-commons-vfs
BuildRequires:	apache-groovy
BuildRequires:	apache-sshd
BuildRequires:	apiguardian
BuildRequires:	asciidoctor-gradle-plugin
BuildRequires:	asciidoctor5-jvm-core-plugin
BuildRequires:	asciidoctorj-api
BuildRequires:	asciidoctorj-groovy-dsl
BuildRequires:	assertj-core
BuildRequires:	auto-common
BuildRequires:	auto-service-annotations
BuildRequires:	auto-value
BuildRequires:	avalon-logkit
BuildRequires:	aws-java-sdk
BuildRequires:	backport9
BuildRequires:	beust-jcommander
BuildRequires:	bouncycastle
BuildRequires:	bsh
BuildRequires:	byte-buddy
BuildRequires:	byte-buddy-agent
BuildRequires:	cdi-api
BuildRequires:	cglib
BuildRequires:	checker-qual
BuildRequires:	codenarc
BuildRequires:	compress-lzf
BuildRequires:	configuration-cache-report
BuildRequires:	crac
BuildRequires:	dd-plist
BuildRequires:	dependency-analysis-gradle-plugin
BuildRequires:	dirgra
BuildRequires:	disruptor
BuildRequires:	dokka
BuildRequires:	dokka-gradle-plugin
BuildRequires:	dom4j
BuildRequires:	eclipse-sisu
BuildRequires:	eddsa
BuildRequires:	error-prone
BuildRequires:	error-prone-annotations
BuildRequires:	escapevelocity
BuildRequires:	fastcsv
BuildRequires:	fastdoubleparser
BuildRequires:	fastutil
BuildRequires:	file-tree-views
BuildRequires:	flexmark
BuildRequires:	freemarker
BuildRequires:	geantyref
BuildRequires:	git
BuildRequires:	gmetrics
BuildRequires:	google-android-annotations
BuildRequires:	google-api-client
BuildRequires:	google-api-services-storage
BuildRequires:	google-gson
BuildRequires:	google-guice
BuildRequires:	google-http-client
BuildRequires:	google-java-format
BuildRequires:	google-oauth-client
BuildRequires:	gradle-bootstrap
BuildRequires:	gradle-errorprone-plugin
BuildRequires:	gradle-fileevents
BuildRequires:	gradle-idea-ext
BuildRequires:	gradle-incap
BuildRequires:	grolifant
BuildRequires:	grpc-context
BuildRequires:	guava
BuildRequires:	guice-parent
BuildRequires:	guice-servlet
BuildRequires:	hamcrest
BuildRequires:	hashmap-util
BuildRequires:	httpcomponents-client
BuildRequires:	httpcomponents-core
BuildRequires:	invokebinder
BuildRequires:	istack-commons-runtime
BuildRequires:	ivy
BuildRequires:	j2objc-annotations
BuildRequires:	jackson-annotations
BuildRequires:	jackson-bom
BuildRequires:	jackson-core
BuildRequires:	jackson-databind
BuildRequires:	jackson-dataformat-cbor
BuildRequires:	jackson-dataformat-xml
BuildRequires:	jackson-dataformat-yaml
BuildRequires:	jackson-datatype-guava
BuildRequires:	jackson-module-kotlin
BuildRequires:	jackson-modules-java8
BuildRequires:	jackson-parent
BuildRequires:	jakarta-activation-api
BuildRequires:	jakarta-annotations
BuildRequires:	jakarta-el
BuildRequires:	jakarta-inject
BuildRequires:	jakarta-xml-bind-api
BuildRequires:	jansi
BuildRequires:	japicmp
BuildRequires:	japicmp-gradle-plugin
BuildRequires:	jatl
BuildRequires:	java-21-openjdk
BuildRequires:	java-21-openjdk-devel
BuildRequires:	java-27-openjdk
BuildRequires:	java-27-openjdk-devel
BuildRequires:	java-caffeine
BuildRequires:	java-cup
BuildRequires:	java-cup-runtime
BuildRequires:	java-diff-utils
BuildRequires:	javacc
BuildRequires:	javaewah
BuildRequires:	javamail
BuildRequires:	javaparser-core
BuildRequires:	javaparser-symbol-solver-core
BuildRequires:	javapoet
BuildRequires:	javassist
BuildRequires:	javax-activation
BuildRequires:	javax.jms
BuildRequires:	javax.servlet
BuildRequires:	javax.xml.bind
BuildRequires:	jaxb-impl
BuildRequires:	jaxen
BuildRequires:	jboss-interceptors-1.2-api
BuildRequires:	jcifs
BuildRequires:	jcl-over-slf4j2
BuildRequires:	jcodings
BuildRequires:	jctools
BuildRequires:	jdependency
BuildRequires:	jdom2
BuildRequires:	jetbrains-annotations
BuildRequires:	jettison
BuildRequires:	jffi
BuildRequires:	jflex
BuildRequires:	jgit
BuildRequires:	jhighlight
BuildRequires:	jitescript
BuildRequires:	jline
BuildRequires:	jmh-gradle-plugin
BuildRequires:	jna
BuildRequires:	jna-platform
BuildRequires:	jnr-a64asm
BuildRequires:	jnr-constants
BuildRequires:	jnr-enxio
BuildRequires:	jnr-ffi
BuildRequires:	jnr-netdb
BuildRequires:	jnr-parent
BuildRequires:	jnr-posix
BuildRequires:	jnr-unixsocket
BuildRequires:	jnr-x86asm
BuildRequires:	joda-convert
BuildRequires:	joda-time
BuildRequires:	joni
BuildRequires:	jquery
BuildRequires:	jrubygradle-resolver
BuildRequires:	json
BuildRequires:	jsoup
BuildRequires:	jspecify
BuildRequires:	jsr-305
BuildRequires:	jul-to-slf4j2
BuildRequires:	junit
BuildRequires:	junit-jupiter
BuildRequires:	junit-platform-testkit
BuildRequires:	junit6
BuildRequires:	junixsocket-common
BuildRequires:	jvm-abi-gen-embeddable
BuildRequires:	jzlib
BuildRequires:	kotlin
BuildRequires:	kotlin-assignment
BuildRequires:	kotlin-assignment-compiler-plugin-embeddable
BuildRequires:	kotlin-build-tools-impl
BuildRequires:	kotlin-compiler-embeddable
BuildRequires:	kotlin-compiler-runner
BuildRequires:	kotlin-gradle-plugin
BuildRequires:	kotlin-gradle-plugin-annotations
BuildRequires:	kotlin-gradle-plugin-api
BuildRequires:	kotlin-libs
BuildRequires:	kotlin-metadata-jvm
BuildRequires:	kotlin-reflect
BuildRequires:	kotlin-sam-with-receiver
BuildRequires:	kotlin-sam-with-receiver-compiler-plugin
BuildRequires:	kotlin-script-runtime
BuildRequires:	kotlin-scripting-common
BuildRequires:	kotlin-scripting-compiler-embeddable
BuildRequires:	kotlin-scripting-compiler-impl-embeddable
BuildRequires:	kotlin-scripting-jvm
BuildRequires:	kotlin-scripting-jvm-host
BuildRequires:	kotlin-stdlib
BuildRequires:	kotlin-time-instant
BuildRequires:	kotlin-tooling-core
BuildRequires:	kotlinx-atomicfu
BuildRequires:	kotlinx-coroutines-core-jvm
BuildRequires:	kotlinx-serialization-core
BuildRequires:	kotlinx-serialization-json
BuildRequires:	kryo
BuildRequires:	log4j
BuildRequires:	log4j-over-slf4j2
BuildRequires:	log4j12
BuildRequires:	maven
BuildRequires:	maven-components
BuildRequires:	maven-shared-utils
BuildRequires:	maven-wagon
BuildRequires:	maven-xml
BuildRequires:	minlog
BuildRequires:	mockito
BuildRequires:	modello
BuildRequires:	moshi
BuildRequires:	moshi-adapters
BuildRequires:	moshi-kotlin
BuildRequires:	moshix
BuildRequires:	moshix-sealed-reflect
BuildRequires:	mwiede-jsch
BuildRequires:	mxparser
BuildRequires:	native-platform
BuildRequires:	netty
BuildRequires:	nullaway
BuildRequires:	oauth-signpost
BuildRequires:	objectweb-asm
BuildRequires:	objenesis
BuildRequires:	okhttp
BuildRequires:	okhttp-digest
BuildRequires:	okio
BuildRequires:	opencensus
BuildRequires:	opentest4j
BuildRequires:	options
BuildRequires:	osgi-core
BuildRequires:	pcollections
BuildRequires:	picocli
BuildRequires:	plexus-build-api
BuildRequires:	plexus-cipher
BuildRequires:	plexus-classworlds
BuildRequires:	plexus-containers-component-annotations
BuildRequires:	plexus-containers-parent
BuildRequires:	plexus-interpolation
BuildRequires:	plexus-pom
BuildRequires:	plexus-sec-dispatcher
BuildRequires:	plexus-utils
BuildRequires:	plexus-xml
BuildRequires:	plugin-publish-plugin
BuildRequires:	plume-util
BuildRequires:	proguard-base
BuildRequires:	proguard-core
BuildRequires:	protobuf-java
BuildRequires:	python
BuildRequires:	qdox
BuildRequires:	ratpack
BuildRequires:	re2j
BuildRequires:	reactive-streams
BuildRequires:	reflectasm
BuildRequires:	reflection-util
BuildRequires:	regexp
BuildRequires:	sbinary
BuildRequires:	sbt-compiler-interface
BuildRequires:	sbt-io
BuildRequires:	sbt-jline
BuildRequires:	sbt-launcher-interface
BuildRequires:	sbt-util-interface
BuildRequires:	sbt-util-logging
BuildRequires:	sbt-util-relation
BuildRequires:	scala
BuildRequires:	scala-parallel-collections
BuildRequires:	scala-parser-combinators
BuildRequires:	scala-xml
BuildRequires:	shaded-jawn-parser
BuildRequires:	shaded-scalajson
BuildRequires:	sjson-new-core
BuildRequires:	sjson-new-scalajson
BuildRequires:	slf4j2
BuildRequires:	snakeyaml
BuildRequires:	software-and-algorithms
BuildRequires:	sonatype-oss-parent
BuildRequires:	spock-core
BuildRequires:	stax2-api
BuildRequires:	stringtemplate4
BuildRequires:	sysjar
BuildRequires:	testng
BuildRequires:	tomlj
BuildRequires:	treelayout
BuildRequires:	unzip
BuildRequires:	woodstox-core
BuildRequires:	xalan-j2
BuildRequires:	xerces-j2
BuildRequires:	xml-apis
BuildRequires:	xml-commons-resolver
BuildRequires:	xmlpull
BuildRequires:	xstream
BuildRequires:	xz-java
BuildRequires:	zero-allocation-hashing
BuildRequires:	zinc
BuildRequires:	zinc-persist-core
Requires:	javapackages-tools
Requires:	java-devel
# The distribution jars embed these libraries and dlopen them.
Requires:	libncursesw.so.6()(64bit)
Requires:	libstdc++.so.6()(64bit)
Requires:	libgcc_s.so.1()(64bit)

%description
Gradle is a build tool with a focus on build automation and support for
multi-language development.
If you are building, testing, publishing, and deploying software on any
platform, Gradle offers a flexible model that can support the entire
development lifecycle from compiling and packaging code to publishing
web sites.
Gradle has been designed to support build automation across multiple
languages and platforms including Java, Scala, Android, C/C++, and
Groovy, and is closely integrated with development tools and
continuous integration servers including Eclipse, IntelliJ, and Jenkins.

%prep
%autosetup -p1
tar -C %{_builddir} -xf %{SOURCE1}

%build
python %{_builddir}/gradle-bootstrap-tools/prepare-bootstrap.py \
	--project %{_builddir}/%{name}-%{version} \
	--tools %{_builddir}/gradle-bootstrap-tools \
	--work %{_builddir}/gradle-work
bash %{_builddir}/gradle-work/run.sh

%install
install -d -m 755 %{buildroot}%{_datadir}/%{name}
install -d -m 755 %{buildroot}%{_bindir}
cd %{_builddir}/%{name}-%{version}/packaging/distributions-full/build/distributions
unzip -q -o ./*-bin.zip
found=
for dist in gradle-*; do
	if test -x "$dist/bin/gradle"; then
		found=$dist
	fi
done
test -n "$found"
/bin/rm -f "$found/bin/gradle.bat"
/bin/cp -a "$found/NOTICE" %{_builddir}/%{name}-%{version}/NOTICE
/bin/cp -a "$found/." %{buildroot}%{_datadir}/%{name}/
chmod 755 %{buildroot}%{_datadir}/%{name}/bin/gradle
ln -s %{_datadir}/%{name}/bin/gradle %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%license LICENSE
%doc NOTICE
