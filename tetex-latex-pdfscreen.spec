Summary:	pdfscreen
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
pdfscreen

%prep
%setup -q -c

%build

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
