%global tl_name lisp-on-tex
%global tl_revision 73165

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.1
Release:	%{tl_revision}.1
Summary:	Execute LISP code in a LaTeX document
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/lisp-on-tex
License:	bsd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lisp-on-tex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lisp-on-tex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a LISP interpreter written using TeX macros; it is
provided as a LaTeX package. The interpreter static scoping, dynamic
typing, and eager evaluation.

