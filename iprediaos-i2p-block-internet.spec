Name:		iprediaos-i2p-block-internet
Version:	0.1
Release:	1%{?dist}
Summary:	Only allow Internet access for i2p

Group:		Applications/Internet
License:	GPL
URL:		http://www.ipredia.org
Source0:	%{name}-%{version}.tar.bz2
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

#BuildRequires:	
Requires:	i2p

%description
IprediaOS I2P Block Internet change iptables to only allow Internet access for the i2p user.


%prep
%setup -q


%build


%install
rm -rf $RPM_BUILD_ROOT
make install PREFIX=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc



%changelog
* Tue Feb 21 2012 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 0.1-1
- Initial spec file
