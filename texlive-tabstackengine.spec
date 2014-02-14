# revision 32944
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-tabstackengine
Version:	20140214
Release:	1
Summary:	TeXLive tabstackengine package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tabstackengine.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tabstackengine.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive tabstackengine package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tabstackengine/tabstackengine.sty
%doc %{_texmfdistdir}/doc/latex/tabstackengine/README
%doc %{_texmfdistdir}/doc/latex/tabstackengine/tabstackengine.pdf
%doc %{_texmfdistdir}/doc/latex/tabstackengine/tabstackengine.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
