Summary:	SIM - Simple Instant Messenger
Name:		sim
Version:	0.8.2
Release:	1
License:	GPL
Url:		http://sim-icq.sourceforge.net/
Group:		Applications/Communications
Source0:	http://telia.dl.sourceforge.net/sourceforge/sim-icq/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	qt-devel 
BuildRequires:	kdelibs-devel 
BuildRequires:	arts-devel

%description
A simple ICQ client with v8 protocol support (2001) for X win system
(requires QT, can be build for KDE). It also runs under MS Windows.

%prep
%setup -q


%build
%{__make}  -f admin/Makefile.common
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}
%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}


%find_lang %{name}

%clean

%files  -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sim
%attr(755,root,root) %{_bindir}/simctrl
%{_datadir}/apps/sim
%{_datadir}/icons/*/*/*/*
%{_desktopdir}/sim.desktop
