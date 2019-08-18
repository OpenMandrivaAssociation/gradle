# FIXME this package is severely broken.
# It should build from source instead of pulling in
# a potentially untrusted binary.

%global __jar_repack 0
%global __provides_exclude_from .*
%global __requires_exclude_from .*
%global __noautoreq '^.*$'
%global __noautoprov '^.*$'

Name:           gradle
Version:	5.6
Release:	1
Summary:        The Gradle build tool
License:        Apache 2.0
URL:            http://gradle.org/
Group:		Development/Tools
BuildArch:      noarch

Source0:        http://services.gradle.org/distributions/gradle-%{version}-bin.zip

Requires:       javapackages-tools
Requires:       java-devel

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
%setup -cT

%install
install -d -m 755 %{buildroot}%{_datadir}/%{name}/
unzip %{SOURCE0}
rm -rf gradle-%{version}/bin/gradle.bat
mv gradle-%{version}/{LICENSE,NOTICE,getting-started.html} .
cp -a gradle-%{version}/* %{buildroot}%{_datadir}/%{name}/
install -d -m 755 %{buildroot}%{_bindir}/
ln -s %{_datadir}/%{name}/bin/gradle %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%doc LICENSE NOTICE getting-started.html
