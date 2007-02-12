Summary:	PDFscreen - redesigning the PDF output for both computer monitor and printing
Summary(pl.UTF-8):	PDFscreen - przetwarzanie wyjścia PDF by nadawało się na monitor i do wydruków
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

%description -l pl.UTF-8
Pakiet PDFscreen pomaga przeprojektowywać wyjście w formacie PDF z
normalnych dokumentów przystosowanych do czytania z komputerowego
monitora zachowując swobodę formatowania dokumentu do konwencjonalnego
wydruku. Zostało to osiągnięte przez przedefiniowanie marginesów i
wysokości/szerokości strony oraz powiązanych wymiarów, aby pasowały do
tych używanych na ekranie komputera. Poprzez zmianę opcji na "print"
(druk) można przełączyć pakiet, by formatował dokument w sposób
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
