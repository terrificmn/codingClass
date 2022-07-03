ampgpu.dc=0을 넣어서 듀얼 모니터를 하려고 할 때

다음에 업데이트가 필요함~ grub2-mkconfig를 하면 (UEFI 방식으로 설치되었을 때)   
grub configuration을 할 때 failed 했다고 나오지만, 
다행이 entry를 추가해주고 실행도 원활하게 잘 된다.

```
[octa@localhost ~]$ sudo cp /etc/default/grub /etc/default/grub-backup
[octa@localhost ~]$ sudo vi /etc/default/grub
[octa@localhost ~]$ sudo grub2-mkconfig -o /boot/grub2/grub.cfg
Generating grub configuration file ...
device-mapper: remove ioctl on osprober-linux-sdb5  failed: Device or resource busy
Command failed.
Found Windows Boot Manager on /dev/sdb1@/EFI/Microsoft/Boot/bootmgfw.efi
Found Ubuntu 20.04.4 LTS (20.04) on /dev/sdb5
Adding boot menu entry for EFI firmware configuration
done
```
