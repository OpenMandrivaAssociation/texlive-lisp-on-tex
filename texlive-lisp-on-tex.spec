# revision 29291
# category Package
# catalog-ctan /macros/latex/contrib/lisp-on-tex
# catalog-date 2013-03-04 11:46:28 +0100
# catalog-license bsd
# catalog-version 1.0
Name:		texlive-lisp-on-tex
Version:	1.0
Release:	4
Summary:	Execute LISP code in a LaTeX document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/lisp-on-tex
License:	BSD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lisp-on-tex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lisp-on-tex.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a LISP interpreter written using TeX
macros; it is provided as a LaTeX package. The interpreter
static scoping, dynamic typing, and eager evaluation.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/lisp-on-tex/lisp-arith.sty
%{_texmfdistdir}/tex/latex/lisp-on-tex/lisp-latexutil.sty
%{_texmfdistdir}/tex/latex/lisp-on-tex/lisp-mod-fpnum.sty
%{_texmfdistdir}/tex/latex/lisp-on-tex/lisp-on-tex.sty
%{_texmfdistdir}/tex/latex/lisp-on-tex/lisp-prim.sty
%{_texmfdistdir}/tex/latex/lisp-on-tex/lisp-read.sty
%{_texmfdistdir}/tex/latex/lisp-on-tex/lisp-string.sty
%{_texmfdistdir}/tex/latex/lisp-on-tex/lisp-util.sty
%doc %{_texmfdistdir}/doc/latex/lisp-on-tex/LICENSE
%doc %{_texmfdistdir}/doc/latex/lisp-on-tex/README
%doc %{_texmfdistdir}/doc/latex/lisp-on-tex/examples/fact.pdf
%doc %{_texmfdistdir}/doc/latex/lisp-on-tex/examples/fact.tex
%doc %{_texmfdistdir}/doc/latex/lisp-on-tex/examples/fpnummodule-mandelbrot.pdf
%doc %{_texmfdistdir}/doc/latex/lisp-on-tex/examples/fpnummodule-mandelbrot.tex
%doc %{_texmfdistdir}/doc/latex/lisp-on-tex/examples/rocket.pdf
%doc %{_texmfdistdir}/doc/latex/lisp-on-tex/examples/rocket.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
