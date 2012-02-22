NAME=$(shell awk '/Name/ { print $$2 }' iprediaos-i2p-block-internet.spec)
VERSION=$(shell awk '/Version/ { print $$2 }' iprediaos-i2p-block-internet.spec)

all:

install: 
	@install -c -m 0755 iprediaos-i2p-block-internet ${PREFIX}/usr/sbin/

archive:
	@git archive --prefix=$(NAME)-$(VERSION)/ HEAD -o $(NAME)-$(VERSION).tar
	@bzip2 -f $(NAME)-$(VERSION).tar
	@echo "$(NAME)-$(VERSION).tar.bz2 created"
clean:
	rm -f *~ *bz2
