Summary:	SIM - Simple Instant Messenger
Summary(pl.UTF-8):	SIM - Simple Instant Messenger - prosty komunikator
Name:		sim
Version:	0.9.4.2
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://download.berlios.de/sim-im/%{name}-%{version}.tar.bz2
# Source0-md5:	80e56dbf394ee8fdcb9dae13647cd6ee
Source1:	%{name}.desktop
Patch0:		kde-ac260-lt.patch
Patch1:		%{name}-am110.patch
URL:		http://sim-icq.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	arts-devel
BuildRequires:	fam-devel
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	kdelibs-devel
BuildRequires:	libart_lgpl-devel
BuildRequires:	libxslt-devel
BuildRequires:	qt-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libXScrnSaver-devel
Requires:	kdelibs >= 9:3.3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Plugins-based instant messenger with support for various protocols.
All protocols support richtext-messages, file transfer, typing
notification, server-side contact list (with postponed synchronization
- you can change contact list in offline mode and after log on all
changes will be synchronized with server), new account registration,
various searches and HTTP-polling. You can use some accounts for each
protocols. Supported protocols: Oscar - ICQ and AIM support, Jabber,
LiveJournal, MSN, Yahoo! and others.

%description -l pl.UTF-8
Prosty komunikator bazujący na wtyczkach ze wsparciem dla różnych
protokołów. Wszystkie protokoły wspierają wiadomości richtext,
transfer plików, sygnalizowanie pisania, lista kontaktów po stronie
serwera (z opóźnioną synchronizacją - możesz zmieniać listę kontaktów
będąc offline - po zalogowaniu online zmiany zostaną zsynchronizowane,
rejestracja nowych kont, różne rodzaje przeszukiwań, pooling HTTP.
Możesz używać niektórych kont dla każdego protokołu. Wspierane
protokołu: Oscar - ICQ oraz AIM, Jabber, LiveJournal, MSN, Yahoo! i
inne.

%prep
%setup -q
%patch0 -p1
%patch1 -p0

%{__perl} -pi -e 's@^sim_plugindir=.*@sim_plugindir="%{_libdir}/sim"@' configure.in.in

%build
%{__make} -f admin/Makefile.common
%configure \
	KDEDIR=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

# it is _not_ in swahili
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/sw
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/sim
%attr(755,root,root) %{_bindir}/simctrl
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{_libdir}/sim
%attr(755,root,root) %{_libdir}/sim/*.so
%{_datadir}/apps/sim
%{_datadir}/services/*.desktop
# already in kdelibs
#%{_datadir}/mimelnk/application/*.desktop
%{_iconsdir}/hicolor/*/*/*.png
%{_desktopdir}/sim.desktop
%{_desktopdir}/kde/sim.desktop
