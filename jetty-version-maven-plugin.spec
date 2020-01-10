Name:           jetty-version-maven-plugin
Version:        1.0.7
Release:        8%{?dist}
Summary:        Jetty version management Maven plugin

License:        ASL 2.0 or EPL
URL:            http://www.eclipse.org/jetty/
Source0:        http://git.eclipse.org/c/jetty/org.eclipse.jetty.toolchain.git/snapshot/%{name}-%{version}.tar.bz2
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven:maven-project)
BuildRequires:  mvn(org.eclipse.jetty.toolchain:jetty-toolchain)


%description
Jetty version management Maven plugin

%package        javadoc
Summary:        API documentation for %{name}

%description    javadoc
%{summary}.


%prep
%setup -q
# copy license files
cp -p jetty-distribution-remote-resources/src/main/resources/* .

# we have java.util stuff in JVM directly now
# https://bugs.eclipse.org/bugs/show_bug.cgi?id=401163
sed -i 's|edu.emory.mathcs.backport.||' \
    jetty-version-maven-plugin/src/main/java/org/eclipse/jetty/toolchain/version/Release.java

%build
pushd %{name}
# skip tests because we don't have jetty-test-helper (yet)
%mvn_build -f

%install
pushd %{name}
%mvn_install


%files -f %{name}/.mfiles
%dir %{_javadir}/%{name}
%doc LICENSE-APACHE-2.0.txt LICENSE-ECLIPSE-1.0.html notice.html

%files javadoc -f %{name}/.mfiles-javadoc
%doc LICENSE-APACHE-2.0.txt LICENSE-ECLIPSE-1.0.html notice.html

%changelog
* Thu Jul 11 2013 Michal Srb <msrb@redhat.com> - 1.0.7-8
- Build with XMvn
- Fix BR

* Tue Feb 19 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.0.7-7
- Fix backport-util-concurrent dependency
- Use file lists

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.0.7-6
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Sep 20 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.7-5
- Install license files

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Nov  4 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.0.7-2
- Add minimal maven version for BR

* Thu Nov  3 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.0.7-1
- Initial version of the package
