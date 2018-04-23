Name:		texlive-tabstackengine
Epoch:		1
Version:	2.10
Release:	1
Summary:	"Tabbing" front-end to stackengine
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tabstackengine
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tabstackengine.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tabstackengine.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a front end to the stackengine package, to
allow tabbed stacking. In most cases, an existing stackengine
command may be prepended with the word "tabbed", "align" or
"tabular" to create a new tabbed version of a stacking macro.
In addition, hooks in the package's parser, that tabbed strings
of data may be parsed, extracted and reconstituted (not
requiring use of any stacking constructions).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tabstackengine
%doc %{_texmfdistdir}/doc/latex/tabstackengine

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
