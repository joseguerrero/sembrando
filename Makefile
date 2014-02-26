# Makefile

SHELL := sh -e

SCRIPTS = "debian/postinst configure"

all: build

test:


	@echo -n "\n===== Comprobando posibles errores de sintaxis en los scripts de mantenedor =====\n\n"

	@for SCRIPT in $(SCRIPTS); \
	do \
		echo -n "$${SCRIPT}\n"; \
		bash -n $${SCRIPT}; \
	done

	@echo -n "\n=================================================================================\nHECHO!\n\n"

build:

	@echo "Nada para compilar!"

install:
	
	mkdir -p $(DESTDIR)/usr/share/sembrando-para-el-futuro
	mkdir -p $(DESTDIR)/usr/share/applications
	mkdir -p $(DESTDIR)/usr/bin
	cp -r src/* $(DESTDIR)/usr/share/sembrando-para-el-futuro/
	cp lanzador/sembrando-para-el-futuro.desktop $(DESTDIR)/usr/share/applications/
	cp bin/sembrando $(DESTDIR)/usr/bin/

uninstall:

	rm -R $(DESTDIR)/usr/share/sembrando-para-el-futuro
	rm $(DESTDIR)/usr/share/applications/sembrando-para-el-futuro.desktop
	rm $(DESTDIR)/usr/bin/sembrando
clean:


reinstall: uninstall install
