Summary:	SIM - Simple Instant Messenger
Summary(pl):	SIM - Simple Instant Messenger - prosty komunikator
Name:		sim
Version:	0.9.3
Release:	2
License:	GPL
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/sim-icq/%{name}-%{version}.tar.gz
# Source0-md5:	c277579df074c31c5dc09a876bde50f4
Source1:	%{name}.desktop
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
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Plugins-based instant messenger with support various protocols. All
protocol support richtext-messages, file transfer, typing
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
rejstracja nowych kont, ró¿ne rodzaje przeszukiwañ, pooling HTTP.
Mo¿esz u¿ywaæ niektórych kont dla ka¿dego protoko³u. Wspierane
protoko³u: Oscar - ICQ oraz AIM, Jabber, LiveJournal, MSN, Yahoo! i
inne.

%prep
%setup -q

%build
%{__make} -f admin/Makefile.common
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
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
%{_datadir}/mimelnk/application/*.desktop
%{_iconsdir}/hicolor/*/*/*.png
%{_desktopdir}/sim.desktop
