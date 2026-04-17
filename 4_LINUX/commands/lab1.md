# Подписывание сертификатов

Подписывающий:
```bash
nc -l -p 8080 > received_name.csr
openssl x509 -req -in received_name.csr -CA root_sakulin_ca.crt -CAkey root_sakulin_ca.key -CAcreateserial -out signed_name_by_sakulin.crt -days 365 -sha256
nc name.duckdns.org 8080 < signed_name_by_sakulin.crt
nc name.duckdns.org 8080 < root_sakulin_ca.crt
```
Подписываемый:
```bash
nc otz.duckdns.org 8080 < site.csr
nc -l -p 8080 > site_signed_by_sakulin.crt
nc -l -p 8080 > root_sakulin_ca.crt
```