%{?scl:%scl_package nodejs-cryptiles}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

Name:       %{?scl_prefix}nodejs-cryptiles
Version:    2.0.5
Release:    1%{?dist}
Summary:    General purpose cryptography utilities for Node.js
License:    BSD
URL:        https://github.com/hueniverse/cryptiles
Source0:    http://registry.npmjs.org/cryptiles/-/cryptiles-%{version}.tgz
BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

BuildRequires:  %{?scl_prefix}nodejs-devel

%description
%{summary}.

%prep
%setup -q -n package

#fix perms
chmod 0644 README.md LICENSE lib/* package.json

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/cryptiles
cp -pr lib package.json %{buildroot}%{nodejs_sitelib}/cryptiles

%nodejs_symlink_deps

#Yet Another Unpackaged Test Framework (lab)
#%%check
#make test

%files
%{nodejs_sitelib}/cryptiles
%doc README.md LICENSE

%changelog
* Wed Sep 21 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.0.5-1
- Updated

* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.2.2-4
- Use macro in -runtime dependency

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.2.2-3
- Rebuilt with updated metapackage

* Thu Oct 17 2013 Tomas Hrcka <thrcka@redhat.com> - 0.2.2-2
- replace provides and requires with macro

* Tue Jul 30 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.2-1
- new upstream release 0.2.2

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.1-1
- new upstream release 0.2.1

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.0-3
- restrict to compatible arches

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.0-2
- add macro for EPEL6 dependency generation

* Fri Apr 12 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.2.0-2
- Add support for software collections 

* Mon Apr 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.0-1
- initial package
