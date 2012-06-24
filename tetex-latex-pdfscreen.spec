Summary:	PDFscreen - redesigning the PDF output for both computer monitor and printing
Summary(pl):	PDFscreen - przetwarzanie wyj�cia PDF by nadawa�o si� na monitor i do wydruk�w
Name:		tetex-latex-pdfscreen
Version:	1.5
Release:	0.1
License:	unknown
Group:		Applications/Publishing/TeX
Source0:	http://www.river-valley.com/download/pdfscreen-%{version}.tar.gz
# Source0-md5:	ddf154211337e883cb59202e5921a5ac
URL:		http://www.river-valley.com/download/
Requires:	tetex-latex
Requires(post,postun):	/usr/bin/texhash
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	pdfscreendir %{_datadir}/texmf/tex/latex/pdfscreen
%define	texhash	[ ! -x %{_bindir}/texhash ] || %{_bindir}/texhash 1>&2 ;

%description
PDFscreen package helps to redesign the PDF output of your normal
documents fit to be read in a computer monitor while retaining the
freedom to format it for conventional printing. This has been brought
about by redefining the margins and page height/width and related
dimensions to fit into that of the computer screen. By changing the
options to "print" you can switch the package to format the document
in the conventional way as per the dictates of your class file.

%description -l pl
Pakiet PDFscreen pomaga przeprojektowywa� wyj�cie w formacie PDF z
normalnych dokument�w przystosowanych do czytania z komputerowego
monitora zachowuj�c swobod� formatowania dokumentu do konwencjonalnego
wydruku. Zosta�o to osi�gni�te przez przedefiniowanie margines�w i
wysoko�ci/szeroko�ci strony oraz powi�zanych wymiar�w, aby pasowa�y do
tych u�ywanych na ekranie komputera. Poprzez zmian� opcji na "print"
(druk) mo�na prze��czy� pakiet, by formatowa� dokument w spos�b
konwencjonalny, jak nakazuje plik klasy.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{pdfscreendir}

install *.sty $RPM_BUILD_ROOT%{pdfscreendir}
install pdfscreen.cfg.specimen $RPM_BUILD_ROOT%{pdfscreendir}/pdfscreen.cfg

%clean
rm -rf $RPM_BUILD_ROOT

%post
%texhash

%postun
%texhash

%files
%defattr(644,root,root,755)
%doc *.pdf
%{pdfscreendir}
