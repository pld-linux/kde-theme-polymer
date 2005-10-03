
%define		_name	polymer

Summary:	KDE style - polymer
Summary(pl):	Styl do KDE - polymer
Name:		kde-theme-%{_name}
Version:	0.4
Release:	2
License:	GPL
Group:		Themes
Source0:	http://www.fosk.it/mart/files/%{_name}.tar.bz2
# Source0-md5:	a151cd6ccba9376fb884d716ff4c4512
URL:		http://www.kde-look.org/content/show.php?content=10919
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freetype-devel
BuildRequires:	kdelibs-devel >= 3.1.2
BuildRequires:	unsermake
Requires:	kdelibs >= 3.1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	kde-style-thin_keramik

%description 
polymer is a KDE based on Keramik.

%description -l pl
polymer to styl KDE oparty na Keramiku.

%package -n kde-style-%{_name}
Summary:	KDE style - %{_name}
Summary(pl):	Styl do KDE - %{_name}
Group:		Themes
Requires:	kdelibs

%description -n kde-style-%{_name}
polymer is modified from keramik as follows:
- Flat Menubar and Toolbar.
- Scrollbar-slider color.(= Window-InactiveBackground)
- Thin push-buttons and scrollbar.
- Selected menu-Item effect.
- Active menubar-Item effect.
- Pixmaps of tabs.
- Active tab effect.
- Striped menu.

%description -n kde-style-%{_name} -l pl
polymer to zmodyfikowany keramik z nastêpuj±cymi zmianami:
- P³askie paski menu i narzêdzi
- Inny kolor suwaka - nieaktywnego t³a
- Cienkie przyciski i suwak
- Efekt dla zaznaczonej i aktywnej pozycji w pasku menu
- Ikonki na zak³adkach
- Efekt aktywnej zak³adki
- Paskowane menu

%package -n kde-colorscheme-%{_name}
Summary:	Color scheme for KDE style - polymer
Summary(pl):	Schemat kolorów do stylu KDE - polymer
Group:		Themes
Requires:	kdelibs

%description -n kde-colorscheme-%{_name}
Color schemes for KDE style - polymer. One of them has a subdued green
look and the second is an interesting yet a little eccentric
green/orange/blue mix.

%description -n kde-colorscheme-%{_name} -l pl
Schematy kolorów do stylu KDE - polymer. Jeden z nich ma stonowany,
zielony wygl±d; drugi jest interesuj±cym, acz trochê ekstrawaganckim
po³±czeniem kolorów: zielonego, pomarañczowego i niebieskiego.

%package -n kde-decoration-%{_name}
Summary:	Kwin decoration - polymer
Summary(pl):	Dekoracja kwin - polymer
Group:		Themes
Requires:	kdebase-desktop

%description -n kde-decoration-%{_name}
A window decoration which goes with the polymer KDE style.
It is similar to the keramik decoration, it differs by:
- having flattened buttons
- extended customizability (like the buttons' shape)

%description -n kde-decoration-%{_name} -l pl
Dekoracja okien, która pasuje do stylu KDE - polymera.
Jest podobna do dekoracji keramika z wyj±tkiem:
- sp³aszczonych przycisków
- zwiêkszonej dostosowywalno¶ci (np. kszta³tu przycisków)

%prep
%setup -q -n %{_name}

%build
#export UNSERMAKE=/usr/share/unsermake/unsermake
cp -f /usr/share/automake/config.sub admin
%{__make} -f Makefile.cvs
%configure \
	--with-qt-libraries=%{_libdir}
%{__make}

%clean
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir="%{_kdedocdir}"

%files -n kde-style-%{_name}
%defattr(644,root,root,755)
%{_libdir}/kde3/plugins/styles/*.la
%attr(755,root,root) %{_libdir}/kde3/plugins/styles/*.so
%{_libdir}/kde3/kstyle_polymer_config.la
%attr(755,root,root) %{_libdir}/kde3/kstyle_polymer_config.so
%{_datadir}/apps/kstyle/themes/*.themerc
##%{_desktopdir}/polymer.desktop

%files -n kde-colorscheme-%{_name}
%defattr(644,root,root,755)
%{_datadir}/apps/kdisplay/color-schemes/*.kcsrc

%files -n kde-decoration-%{_name}
%defattr(644,root,root,755)
%attr(755,root,root)%{_libdir}/kde3/kwin*.so
%{_libdir}/kde3/kwin*.la
%{_datadir}/apps/kwin/*.desktop
