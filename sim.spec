Summary:	SIM - Simple Instant Messenger
Summary(pl):	SIM - Simple Instant Messenger - prosty komunikator
Name:		sim
Version:	0.8.3
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/sourceforge/sim-icq/%{name}-%{version}.tar.gz
# Source0-md5:	a981b7aa4330bf050a46e144942d2726
Source1:	%{name}.desktop
URL:		http://sim-icq.sourceforge.net/
BuildRequires:	arts-devel
BuildRequires:	fam-devel
BuildRequires:	kdelibs-devel
BuildRequires:	libart_lgpl-devel
BuildRequires:	qt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A simple ICQ client with v8 protocol support (2001) for X Window
system (requires QT, can be build for KDE). It also runs under MS
Windows.

%description -l pl
Prosty klient ICQ z obs³ug± protoko³u v8 (2001) dla systemu X Window
(wymaga QT, mo¿e byæ zbudowany dla KDE). Dzia³a tak¿e pod MS Windows.

%prep
%setup -q

%build
kde_icondir="%{_pixmapsdir}"; export kde_icondir
%{__make} -f admin/Makefile.common
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files  -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sim
%attr(755,root,root) %{_bindir}/simctrl
%{_datadir}/apps/sim
%{_pixmapsdir}/*/*/*/*
%{_desktopdir}/sim.desktop
