# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
ASSETSDIR     = assets
SOURCEDIR     = source
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

serve:
	@python -m http.server -d ./$(BUILDDIR)/html

deploy:
	@sphinx-multiversion $(SOURCEDIR) $(BUILDDIR)/html
	@cp $(ASSETSDIR)/redirect.html $(BUILDDIR)/html/index.html
	@surge $(BUILDDIR)/html molduck.surge.sh

watch:
	@sphinx-autobuild $(SOURCEDIR) $(BUILDDIR)/html --port 5555

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
