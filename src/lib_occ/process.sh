#!/usr/bin/bash
all_args=("$@")
first_arg="$1"
second_args="$2"
rest_args=("${all_args[@]:2}")

case $1 in
        www-data)
            exec php  /var/www/nextcloud/occ ${rest_args[@]}
        ;;
        *)

            exec sudo -u  www-data php  /var/www/nextcloud/occ ${rest_args[@]}
        ;;
esac