
MAKEFILE_DIR:=$(dir $(abspath $(lastword $(MAKEFILE_LIST))))

all :
	rm -rf $(MAKEFILE_DIR)/build
	$(MAKEFILE_DIR)/packages/python/bin/sphinx-build -M html \
		$(MAKEFILE_DIR)/doc/source $(MAKEFILE_DIR)/build
	touch $(MAKEFILE_DIR)/build/html/.nojekyll

