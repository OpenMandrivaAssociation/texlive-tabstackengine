Name:		texlive-tabstackengine
Epoch:		1
Version:	46848
Release:	2
Summary:	"Tabbing" front-end to stackengine
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tabstackengine
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tabstackengine.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tabstackengine.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
