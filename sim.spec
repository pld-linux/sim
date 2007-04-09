Summary:	SIM - Simple Instant Messenger
Summary(pl):	SIM - Simple Instant Messenger - prosty komunikator
Name:		sim
Version:	0.9.4.3
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://download.berlios.de/sim-im/%{name}-%{version}.tar.bz2
# Source0-md5:	4bc30577e619e05252d394d51dc20747
Source1:	%{name}.desktop
Patch0:		kde-ac260-lt.patch
Patch1:		%{name}-am110.patch
URL:		http://sim-icq.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	arts-devel
BuildRequires:	fam-devel
BuildRequires:	flex
BuildRequires:	kdelibs-devel >= 9:3.3.0
BuildRequires:	libart_lgpl-devel
BuildRequires:	libxslt-devel
BuildRequires:	qt-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pkgconfig
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

%description -l pl
Prosty komunikator bazuj±cy na wtyczkach ze wsparciem dla ró¿nych
protoko³ów. Wszystkie protoko³y wspieraj± wiadomo¶ci richtext,
transfer plików, sygnalizowanie pisania, lista kontaktów po stronie
serwera (z opó¼nion± synchronizacj± - mo¿esz zmieniaæ listê kontaktów
bêd±c offline - po zalogowaniu online zmiany zostan± zsynchronizowane,
rejestracja nowych kont, ró¿ne rodzaje przeszukiwañ, pooling HTTP.
Mo¿esz u¿ywaæ niektórych kont dla ka¿dego protoko³u. Wspierane
protoko³u: Oscar - ICQ oraz AIM, Jabber, LiveJournal, MSN, Yahoo! i
inne.

%prep
%setup -q
%patch0 -p1
%patch1 -p0

%{__perl} -pi -e 's@^sim_plugindir=.*@sim_plugindir="%{_libdir}/sim"@' configure.in.in

%build
%{__make} -f admin/Makefile.common cvs
%configure \
	KDEDIR=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/kde

# it is _not_ in swahili
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/sw

# remove .la files
rm $RPM_BUILD_ROOT%{_libdir}/libsim.la
rm $RPM_BUILD_ROOT%{_libdir}/sim/*.la

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
%{_desktopdir}/kde/sim.desktop
