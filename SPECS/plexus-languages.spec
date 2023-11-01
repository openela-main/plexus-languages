Name:           plexus-languages
Version:        0.9.10
Release:        3%{?dist}
Summary:        Plexus Languages
License:        ASL 2.0
URL:            https://github.com/codehaus-plexus/plexus-languages
BuildArch:      noarch

# ./generate-tarball.sh
Source0:        %{name}-%{version}.tar.gz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
# Sources contain bundled jars that we cannot verify for licensing
Source2:        generate-tarball.sh

BuildRequires:  maven-local
BuildRequires:  mvn(com.thoughtworks.qdox:qdox)
BuildRequires:  mvn(javax.inject:javax.inject)
BuildRequires:  mvn(org.apache.maven.plugins:maven-failsafe-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus:pom:)
BuildRequires:  mvn(org.ow2.asm:asm)

%description
Plexus Languages is a set of Plexus components that maintain shared
language features.

%{?javadoc_package}

%prep
%setup -q -n plexus-languages-plexus-languages-%{version}

cp %{SOURCE1} .

%build
# we don't have mockito 2 yet + many tests rely on bundled test jars/classes
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%license LICENSE-2.0.txt

%changelog
* Mon Jul 23 2018 Michael Simacek <msimacek@redhat.com> - 0.9.10-3
- Repack tarball without bundled jars

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Michael Simacek <msimacek@redhat.com> - 0.9.10-1
- Update to upstream version 0.9.10

* Fri Jun 29 2018 Michael Simacek <msimacek@redhat.com> - 0.9.3-5
- Disable broken test

* Wed Feb 14 2018 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.9.3-4
- Generate javadoc package automatically

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep 12 2017 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.9.3-2
- Replace JARs used as test resources with symlinks to system JARs

* Mon Sep 11 2017 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.9.3-1
- Initial packaging
