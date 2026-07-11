%global tl_name tabstackengine
%global tl_revision 46848

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.10
Release:	%{tl_revision}.1
Summary:	Tabbing front-end to stackengine
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tabstackengine
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tabstackengine.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tabstackengine.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a front end to the stackengine package, to allow
tabbed stacking. In most cases, an existing stackengine command may be
prepended with the word "tabbed", "align" or "tabular" to create a new
tabbed version of a stacking macro. In addition, hooks in the package's
parser that tabbed strings of data may be parsed, extracted, and
reconstituted (not requiring use of any stacking constructions).

