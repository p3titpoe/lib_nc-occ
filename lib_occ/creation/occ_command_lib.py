### Definition Library
common = {
     'check': {'command': 'check', 'desc': 'check dependencies of the server environment', 'path': ['check']},
     'completion': {'command': 'completion', 'desc': ' Dump the shell completion script', 'path': ['completion']},
     'help': {'command': 'help', 'desc': ' Display help for a command', 'path': ['help']},
     'list': {'command': 'list', 'desc': ' List commands', 'path': ['list']},
     'setupchecks': {'command': 'setupchecks', 'desc': 'Run setup checks and output the results', 'path': ['setupchecks']},
     'status': {'command': 'status', 'desc': ' show some status information', 'path': ['status']},
     'upgrade': {'command': 'upgrade', 'desc': 'run upgrade routines after installation of a new release The release has to be installed before', 'path': ['upgrade']},
     'occ_lib_name':'common'
}
activity = {
         'send-mails': {'command': 'activity:send-mails', 'desc': 'Sends the activity notification mails', 'path': ['activity', 'send-mails']},
     'occ_lib_name':'activity'
}
admindelegation = {
     'add': {'command': 'admin-delegation:add', 'desc': ' add setting delegation to a group', 'path': ['admin-delegation', 'add']},
     'remove': {'command': 'admin-delegation:remove', 'desc': 'remove settings delegation from a group', 'path': ['admin-delegation', 'remove']},
     'show': {'command': 'admin-delegation:show', 'desc': 'show delegated settings', 'path': ['admin-delegation', 'show']},
     'occ_lib_name':'admindelegation'
}
app = {
         'disable': {'command': 'app:disable', 'desc': 'disable an app', 'path': ['app', 'disable']},
         'enable': {'command': 'app:enable', 'desc': ' enable an app', 'path': ['app', 'enable']},
         'getpath': {'command': 'app:getpath', 'desc': 'Get an absolute path to the app directory', 'path': ['app', 'getpath']},
         'install': {'command': 'app:install', 'desc': 'install an app', 'path': ['app', 'install']},
         'list': {'command': 'app:list', 'desc': ' List all available apps', 'path': ['app', 'list']},
         'remove': {'command': 'app:remove', 'desc': ' remove an app', 'path': ['app', 'remove']},
         'update': {'command': 'app:update', 'desc': ' update an app or all apps', 'path': ['app', 'update']},
     'occ_lib_name':'app'
}
appapi = {
         'app':{
                 'config':{
                         'delete': {'command': 'app_api:app:config:delete', 'desc': 'Delete ExApp configs', 'path': ['app_api', 'app', 'config', 'delete']},
                         'get': {'command': 'app_api:app:config:get', 'desc': ' Get ExApp config', 'path': ['app_api', 'app', 'config', 'get']},
                         'list': {'command': 'app_api:app:config:list', 'desc': 'List ExApp configs', 'path': ['app_api', 'app', 'config', 'list']},
                         'set': {'command': 'app_api:app:config:set', 'desc': ' Set ExApp config', 'path': ['app_api', 'app', 'config', 'set']},
                },
                 'disable': {'command': 'app_api:app:disable', 'desc': 'Disable registered external app', 'path': ['app_api', 'app', 'disable']},
                 'enable': {'command': 'app_api:app:enable', 'desc': ' Enable registered external app', 'path': ['app_api', 'app', 'enable']},
                 'list': {'command': 'app_api:app:list', 'desc': ' List ExApps', 'path': ['app_api', 'app', 'list']},
                 'register': {'command': 'app_api:app:register', 'desc': ' Install external App', 'path': ['app_api', 'app', 'register']},
                 'unregister': {'command': 'app_api:app:unregister', 'desc': ' Unregister external app', 'path': ['app_api', 'app', 'unregister']},
                 'update': {'command': 'app_api:app:update', 'desc': ' Update ExApp', 'path': ['app_api', 'app', 'update']},
        },
         'daemon':{
                 'list': {'command': 'app_api:daemon:list', 'desc': 'List registered daemons', 'path': ['app_api', 'daemon', 'list']},
                 'register': {'command': 'app_api:daemon:register', 'desc': 'Register daemon config for ExApp deployment', 'path': ['app_api', 'daemon', 'register']},
                 'registry':{
                         'add': {'command': 'app_api:daemon:registry:add', 'desc': 'Add Deploy daemon Docker registry mapping', 'path': ['app_api', 'daemon', 'registry', 'add']},
                         'list': {'command': 'app_api:daemon:registry:list', 'desc': ' List configured Deploy daemon Docker registry mappings', 'path': ['app_api', 'daemon', 'registry', 'list']},
                         'remove': {'command': 'app_api:daemon:registry:remove', 'desc': ' Remove Deploy daemon Docker registry mapping', 'path': ['app_api', 'daemon', 'registry', 'remove']},
                },
                 'unregister': {'command': 'app_api:daemon:unregister', 'desc': 'Unregister daemon', 'path': ['app_api', 'daemon', 'unregister']},
        },
     'occ_lib_name':'appapi'
}
background = {
         'cron': {'command': 'background:cron', 'desc': 'backgroundajaxbackgroundwebcron Use cron ajax or webcron to run background jobs', 'path': ['background', 'cron']},
     'occ_lib_name':'background'
}
backgroundjob = {
         'delete': {'command': 'background-job:delete', 'desc': 'Remove a background job from database', 'path': ['background-job', 'delete']},
         'execute': {'command': 'background-job:execute', 'desc': ' Execute a single background job manually', 'path': ['background-job', 'execute']},
         'list': {'command': 'background-job:list', 'desc': 'List background jobs', 'path': ['background-job', 'list']},
         'worker': {'command': 'background-job:worker', 'desc': 'Run a background job worker', 'path': ['background-job', 'worker']},
     'occ_lib_name':'backgroundjob'
}
bookmarks = {
         'clear-previews': {'command': 'bookmarks:clear-previews', 'desc': ' Clear all cached bookmarks previews so that they have to be regenerated', 'path': ['bookmarks', 'clear-previews']},
     'occ_lib_name':'bookmarks'
}
broadcast = {
         'test': {'command': 'broadcast:test', 'desc': ' test the SSE broadcaster', 'path': ['broadcast', 'test']},
     'occ_lib_name':'broadcast'
}
calendar = {
         'export': {'command': 'calendar:export', 'desc': 'Export calendar data from supported calendars to disk or stdout', 'path': ['calendar', 'export']},
         'import': {'command': 'calendar:import', 'desc': 'Import calendar data to supported calendars from disk or stdin', 'path': ['calendar', 'import']},
     'occ_lib_name':'calendar'
}
circles = {
         'check': {'command': 'circles:check', 'desc': 'Checking your configuration', 'path': ['circles', 'check']},
         'maintenance': {'command': 'circles:maintenance', 'desc': 'Clean stuff keeps the app running', 'path': ['circles', 'maintenance']},
         'manage':{
                 'config': {'command': 'circles:manage:config', 'desc': 'edit configtype of a Team', 'path': ['circles', 'manage', 'config']},
                 'create': {'command': 'circles:manage:create', 'desc': 'create a new team', 'path': ['circles', 'manage', 'create']},
                 'destroy': {'command': 'circles:manage:destroy', 'desc': ' destroy a circle by its ID', 'path': ['circles', 'manage', 'destroy']},
                 'details': {'command': 'circles:manage:details', 'desc': ' get details about a team by its ID', 'path': ['circles', 'manage', 'details']},
                 'edit': {'command': 'circles:manage:edit', 'desc': 'Team', 'path': ['circles', 'manage', 'edit']},
                 'join': {'command': 'circles:manage:join', 'desc': 'emulate a user joining a Team', 'path': ['circles', 'manage', 'join']},
                 'leave': {'command': 'circles:manage:leave', 'desc': ' simulate a user joining a Team', 'path': ['circles', 'manage', 'leave']},
                 'list': {'command': 'circles:manage:list', 'desc': 'listing current teams', 'path': ['circles', 'manage', 'list']},
                 'setting': {'command': 'circles:manage:setting', 'desc': ' edit setting for a Team', 'path': ['circles', 'manage', 'setting']},
        },
         'members':{
                 'add': {'command': 'circles:members:add', 'desc': 'Add a member to a Team', 'path': ['circles', 'members', 'add']},
                 'details': {'command': 'circles:members:details', 'desc': 'get details about a member by its ID', 'path': ['circles', 'members', 'details']},
                 'level': {'command': 'circles:members:level', 'desc': 'Change the level of a member from a Team', 'path': ['circles', 'members', 'level']},
                 'list': {'command': 'circles:members:list', 'desc': ' listing Members from a Team', 'path': ['circles', 'members', 'list']},
                 'remove': {'command': 'circles:members:remove', 'desc': ' remove a member from a team', 'path': ['circles', 'members', 'remove']},
                 'search': {'command': 'circles:members:search', 'desc': ' Change the level of a member from a Team', 'path': ['circles', 'members', 'search']},
        },
         'memberships': {'command': 'circles:memberships', 'desc': 'index and display memberships for local and federated users', 'path': ['circles', 'memberships']},
         'migrate':{
                 'customgroups': {'command': 'circles:migrate:customgroups', 'desc': ' ', 'path': ['circles', 'migrate', 'customgroups']},
        },
         'remote': {'command': 'circles:remote', 'desc': ' remote features', 'path': ['circles', 'remote']},
         'shares':{
                 'files': {'command': 'circles:shares:files', 'desc': ' listing shares files', 'path': ['circles', 'shares', 'files']},
        },
         'sync': {'command': 'circles:sync', 'desc': ' Sync Circles and Members', 'path': ['circles', 'sync']},
         'test': {'command': 'circles:test', 'desc': ' testing some features', 'path': ['circles', 'test']},
     'occ_lib_name':'circles'
}
config = {
         'app':{
                 'delete': {'command': 'config:app:delete', 'desc': 'Delete an app config value', 'path': ['config', 'app', 'delete']},
                 'get': {'command': 'config:app:get', 'desc': ' Get an app config value', 'path': ['config', 'app', 'get']},
                 'set': {'command': 'config:app:set', 'desc': ' Set an app config value', 'path': ['config', 'app', 'set']},
        },
         'import': {'command': 'config:import', 'desc': 'Import a list of configs', 'path': ['config', 'import']},
         'list': {'command': 'config:list', 'desc': 'List all configs', 'path': ['config', 'list']},
         'preset': {'command': 'config:preset', 'desc': 'Select a config preset', 'path': ['config', 'preset']},
         'system':{
                 'delete': {'command': 'config:system:delete', 'desc': ' Delete a system config value', 'path': ['config', 'system', 'delete']},
                 'get': {'command': 'config:system:get', 'desc': 'Get a system config value', 'path': ['config', 'system', 'get']},
                 'set': {'command': 'config:system:set', 'desc': 'Set a system config value', 'path': ['config', 'system', 'set']},
        },
     'occ_lib_name':'config'
}
dav = {
         'absence':{
                 'get': {'command': 'dav:absence:get', 'desc': '', 'path': ['dav', 'absence', 'get']},
                 'set': {'command': 'dav:absence:set', 'desc': '', 'path': ['dav', 'absence', 'set']},
        },
         'clear-calendar-unshares': {'command': 'dav:clear-calendar-unshares', 'desc': 'Clear calendar unshares for a user', 'path': ['dav', 'clear-calendar-unshares']},
         'clear-contacts-photo-cache': {'command': 'dav:clear-contacts-photo-cache', 'desc': ' Clear cached contact photos', 'path': ['dav', 'clear-contacts-photo-cache']},
         'create-addressbook': {'command': 'dav:create-addressbook', 'desc': ' Create a dav addressbook', 'path': ['dav', 'create-addressbook']},
         'create-calendar': {'command': 'dav:create-calendar', 'desc': 'Create a dav calendar', 'path': ['dav', 'create-calendar']},
         'create-subscription': {'command': 'dav:create-subscription', 'desc': 'Create a dav subscription', 'path': ['dav', 'create-subscription']},
         'delete-calendar': {'command': 'dav:delete-calendar', 'desc': 'Delete a dav calendar', 'path': ['dav', 'delete-calendar']},
         'delete-subscription': {'command': 'dav:delete-subscription', 'desc': 'Delete a calendar subscription for a user', 'path': ['dav', 'delete-subscription']},
         'fix-missing-caldav-changes': {'command': 'dav:fix-missing-caldav-changes', 'desc': ' Insert missing calendarchanges rows for existing events', 'path': ['dav', 'fix-missing-caldav-changes']},
         'list-addressbooks': {'command': 'dav:list-addressbooks', 'desc': 'List all addressbooks of a user', 'path': ['dav', 'list-addressbooks']},
         'list-calendar-shares': {'command': 'dav:list-calendar-shares', 'desc': ' List all calendar shares for a user', 'path': ['dav', 'list-calendar-shares']},
         'list-calendars': {'command': 'dav:list-calendars', 'desc': ' List all calendars of a user', 'path': ['dav', 'list-calendars']},
         'list-subscriptions': {'command': 'dav:list-subscriptions', 'desc': ' List all calendar subscriptions for a user', 'path': ['dav', 'list-subscriptions']},
         'move-calendar': {'command': 'dav:move-calendar', 'desc': 'Move a calendar from an user to another', 'path': ['dav', 'move-calendar']},
         'remove-invalid-shares': {'command': 'dav:remove-invalid-shares', 'desc': 'Remove invalid dav shares', 'path': ['dav', 'remove-invalid-shares']},
         'retention':{
                 'clean-up': {'command': 'dav:retention:clean-up', 'desc': ' ', 'path': ['dav', 'retention', 'clean-up']},
        },
         'send-event-reminders': {'command': 'dav:send-event-reminders', 'desc': ' Sends event reminders', 'path': ['dav', 'send-event-reminders']},
         'sync-birthday-calendar': {'command': 'dav:sync-birthday-calendar', 'desc': ' Synchronizes the birthday calendar', 'path': ['dav', 'sync-birthday-calendar']},
         'sync-system-addressbook': {'command': 'dav:sync-system-addressbook', 'desc': 'Synchronizes users to the system addressbook', 'path': ['dav', 'sync-system-addressbook']},
     'occ_lib_name':'dav'
}
db = {
         'add-missing-columns': {'command': 'db:add-missing-columns', 'desc': ' Add missing optional columns to the database tables', 'path': ['db', 'add-missing-columns']},
         'add-missing-indices': {'command': 'db:add-missing-indices', 'desc': ' Add missing indices to the database tables', 'path': ['db', 'add-missing-indices']},
         'add-missing-primary-keys': {'command': 'db:add-missing-primary-keys', 'desc': 'Add missing primary keys to the database tables', 'path': ['db', 'add-missing-primary-keys']},
         'convert-filecache-bigint': {'command': 'db:convert-filecache-bigint', 'desc': 'Convert the ID columns of the filecache to BigInt', 'path': ['db', 'convert-filecache-bigint']},
         'convert-mysql-charset': {'command': 'db:convert-mysql-charset', 'desc': ' Convert charset of MySQLMariaDB to use utf8mb4', 'path': ['db', 'convert-mysql-charset']},
         'convert-type': {'command': 'db:convert-type', 'desc': 'Convert the Nextcloud database to the newly configured one', 'path': ['db', 'convert-type']},
         'schema':{
                 'expected': {'command': 'db:schema:expected', 'desc': ' Export the expected database schema for a fresh installation', 'path': ['db', 'schema', 'expected']},
                 'export': {'command': 'db:schema:export', 'desc': ' Export the current database schema', 'path': ['db', 'schema', 'export']},
        },
     'occ_lib_name':'db'
}
encryption = {
         'change-key-storage-root': {'command': 'encryption:change-key-storage-root', 'desc': ' Change key storage root', 'path': ['encryption', 'change-key-storage-root']},
         'decrypt-all': {'command': 'encryption:decrypt-all', 'desc': ' Disable serverside encryption and decrypt all files', 'path': ['encryption', 'decrypt-all']},
         'disable': {'command': 'encryption:disable', 'desc': ' Disable encryption', 'path': ['encryption', 'disable']},
         'enable': {'command': 'encryption:enable', 'desc': 'Enable encryption', 'path': ['encryption', 'enable']},
         'encrypt-all': {'command': 'encryption:encrypt-all', 'desc': ' Encrypt all files for all users', 'path': ['encryption', 'encrypt-all']},
         'list-modules': {'command': 'encryption:list-modules', 'desc': 'List all available encryption modules', 'path': ['encryption', 'list-modules']},
         'migrate-key-storage-format': {'command': 'encryption:migrate-key-storage-format', 'desc': 'Migrate the format of the keystorage to a newer format', 'path': ['encryption', 'migrate-key-storage-format']},
         'set-default-module': {'command': 'encryption:set-default-module', 'desc': 'Set the encryption default module', 'path': ['encryption', 'set-default-module']},
         'show-key-storage-root': {'command': 'encryption:show-key-storage-root', 'desc': ' Show current key storage root', 'path': ['encryption', 'show-key-storage-root']},
         'status': {'command': 'encryption:status', 'desc': 'Lists the current status of encryption', 'path': ['encryption', 'status']},
     'occ_lib_name':'encryption'
}
federation = {
         'sync-addressbooks': {'command': 'federation:sync-addressbooks', 'desc': ' Synchronizes addressbooks of all federated clouds', 'path': ['federation', 'sync-addressbooks']},
         'sync-calendars': {'command': 'federation:sync-calendars', 'desc': 'Synchronize all incoming federated calendar shares', 'path': ['federation', 'sync-calendars']},
     'occ_lib_name':'federation'
}
files = {
         'cleanup': {'command': 'files:cleanup', 'desc': 'Clean up orphaned filecache and mount entries', 'path': ['files', 'cleanup']},
         'copy': {'command': 'files:copy', 'desc': ' Copy a file or folder', 'path': ['files', 'copy']},
         'delete': {'command': 'files:delete', 'desc': ' Delete a file or folder', 'path': ['files', 'delete']},
         'get': {'command': 'files:get', 'desc': 'Get the contents of a file', 'path': ['files', 'get']},
         'move': {'command': 'files:move', 'desc': ' Move a file or folder', 'path': ['files', 'move']},
         'object':{
                 'delete': {'command': 'files:object:delete', 'desc': 'Delete an object from the object store', 'path': ['files', 'object', 'delete']},
                 'get': {'command': 'files:object:get', 'desc': ' Get the contents of an object', 'path': ['files', 'object', 'get']},
                 'info': {'command': 'files:object:info', 'desc': 'Get the metadata of an object', 'path': ['files', 'object', 'info']},
                 'list': {'command': 'files:object:list', 'desc': 'List all objects in the object store', 'path': ['files', 'object', 'list']},
                 'multi':{
                         'rename-config': {'command': 'files:object:multi:rename-config', 'desc': ' Rename an object store configuration and move all users over to the new configuration', 'path': ['files', 'object', 'multi', 'rename-config']},
                         'users': {'command': 'files:object:multi:users', 'desc': ' Get the mapping between users and object store buckets', 'path': ['files', 'object', 'multi', 'users']},
                },
                 'orphans': {'command': 'files:object:orphans', 'desc': ' List all objects in the object store that dont have a matching entry in the database', 'path': ['files', 'object', 'orphans']},
                 'put': {'command': 'files:object:put', 'desc': ' Write a file to the object store', 'path': ['files', 'object', 'put']},
        },
         'put': {'command': 'files:put', 'desc': 'Write contents of a file', 'path': ['files', 'put']},
         'recommendations':{
                 'recommend': {'command': 'files:recommendations:recommend', 'desc': 'Shows recommended files for an account', 'path': ['files', 'recommendations', 'recommend']},
        },
         'reminders': {'command': 'files:reminders', 'desc': 'List file reminders', 'path': ['files', 'reminders']},
         'repair-tree': {'command': 'files:repair-tree', 'desc': 'Try and repair malformed filesystem tree structures', 'path': ['files', 'repair-tree']},
         'sanitize-filenames': {'command': 'files:sanitize-filenames', 'desc': ' Renames files to match naming constraints', 'path': ['files', 'sanitize-filenames']},
         'scan': {'command': 'files:scan', 'desc': ' rescan filesystem', 'path': ['files', 'scan']},
         'scan-app-data': {'command': 'files:scan-app-data', 'desc': 'rescan the AppData folder', 'path': ['files', 'scan-app-data']},
         'transfer-ownership': {'command': 'files:transfer-ownership', 'desc': ' All files and folders are moved to another user  outgoing shares and incoming user file shares optionally are moved as well', 'path': ['files', 'transfer-ownership']},
         'windows-compatible-filenames': {'command': 'files:windows-compatible-filenames', 'desc': ' Enforce naming constraints for windows compatible filenames', 'path': ['files', 'windows-compatible-filenames']},
     'occ_lib_name':'files'
}
group = {
         'add': {'command': 'group:add', 'desc': 'Add a group', 'path': ['group', 'add']},
         'adduser': {'command': 'group:adduser', 'desc': 'add a user to a group', 'path': ['group', 'adduser']},
         'delete': {'command': 'group:delete', 'desc': ' Remove a group', 'path': ['group', 'delete']},
         'info': {'command': 'group:info', 'desc': ' Show information about a group', 'path': ['group', 'info']},
         'list': {'command': 'group:list', 'desc': ' list configured groups', 'path': ['group', 'list']},
         'removeuser': {'command': 'group:removeuser', 'desc': ' remove a user from a group', 'path': ['group', 'removeuser']},
     'occ_lib_name':'group'
}
info = {
     'file':{
             'info:file': {'command': 'info:file', 'desc': 'get information for a file', 'path': ['info', 'file'], 'space': {'command': 'info:file:space', 'desc': 'Summarize space usage of specified folder', 'path': ['info', 'file', 'space']}},
    },
     'storage': {'command': 'info:storage', 'desc': ' Get information a single storage', 'path': ['info', 'storage']},
     'storages': {'command': 'info:storages', 'desc': 'List storages ordered by the number of files', 'path': ['info', 'storages']},
     'occ_lib_name':'info'
}
integrity = {
         'check-app': {'command': 'integrity:check-app', 'desc': 'Check integrity of an app using a signature', 'path': ['integrity', 'check-app']},
         'check-core': {'command': 'integrity:check-core', 'desc': ' Check integrity of core code using a signature', 'path': ['integrity', 'check-core']},
         'sign-app': {'command': 'integrity:sign-app', 'desc': ' Signs an app using a private key', 'path': ['integrity', 'sign-app']},
         'sign-core': {'command': 'integrity:sign-core', 'desc': 'Sign core using a private key', 'path': ['integrity', 'sign-core']},
     'occ_lib_name':'integrity'
}
l10n = {
         'createjs': {'command': 'l10n:createjs', 'desc': 'Create javascript translation files for a given app', 'path': ['l10n', 'createjs']},
     'occ_lib_name':'l10n'
}
log = {
         'file': {'command': 'log:file', 'desc': ' manipulate logging backend', 'path': ['log', 'file']},
         'manage': {'command': 'log:manage', 'desc': ' manage logging configuration', 'path': ['log', 'manage']},
         'tail': {'command': 'log:tail', 'desc': ' Tail the nextcloud logfile', 'path': ['log', 'tail']},
         'watch': {'command': 'log:watch', 'desc': 'Watch the nextcloud logfile', 'path': ['log', 'watch']},
     'occ_lib_name':'log'
}
maintenance = {
         'data-fingerprint': {'command': 'maintenance:data-fingerprint', 'desc': ' update the systems datafingerprint after a backup is restored', 'path': ['maintenance', 'data-fingerprint']},
         'mimetype':{
                 'update-db': {'command': 'maintenance:mimetype:update-db', 'desc': ' Update database mimetypes and update filecache', 'path': ['maintenance', 'mimetype', 'update-db']},
                 'update-js': {'command': 'maintenance:mimetype:update-js', 'desc': ' Update mimetypelistjs', 'path': ['maintenance', 'mimetype', 'update-js']},
        },
         'mode': {'command': 'maintenance:mode', 'desc': ' Show or toggle maintenance mode status', 'path': ['maintenance', 'mode']},
         'repair': {'command': 'maintenance:repair', 'desc': ' repair this installation', 'path': ['maintenance', 'repair']},
         'repair-share-owner': {'command': 'maintenance:repair-share-owner', 'desc': ' repair invalid shareowner entries in the database', 'path': ['maintenance', 'repair-share-owner']},
         'theme':{
                 'update': {'command': 'maintenance:theme:update', 'desc': ' Apply custom theme changes', 'path': ['maintenance', 'theme', 'update']},
        },
         'update':{
                 'htaccess': {'command': 'maintenance:update:htaccess', 'desc': 'Updates the htaccess file', 'path': ['maintenance', 'update', 'htaccess']},
        },
     'occ_lib_name':'maintenance'
}
memcache = {
         'distributed':{
                 'clear': {'command': 'memcache:distributed:clear', 'desc': ' Clear values from the distributed memcache', 'path': ['memcache', 'distributed', 'clear']},
                 'delete': {'command': 'memcache:distributed:delete', 'desc': 'Delete a value in the distributed memcache', 'path': ['memcache', 'distributed', 'delete']},
                 'get': {'command': 'memcache:distributed:get', 'desc': ' Get a value from the distributed memcache', 'path': ['memcache', 'distributed', 'get']},
                 'set': {'command': 'memcache:distributed:set', 'desc': ' Set a value in the distributed memcache', 'path': ['memcache', 'distributed', 'set']},
        },
         'redis': {'command': {'command': 'memcache:redis:command', 'desc': ' Send raw redis command to the configured redis server', 'path': ['memcache', 'redis', 'command']}},
     'occ_lib_name':'memcache'
}
metadata = {
         'get': {'command': 'metadata:get', 'desc': ' get stored metadata about a file by its id', 'path': ['metadata', 'get']},
     'occ_lib_name':'metadata'
}
migrations = {
         'preview': {'command': 'migrations:preview', 'desc': ' Get preview of available DB migrations in case of initiating an upgrade', 'path': ['migrations', 'preview']},
     'occ_lib_name':'migrations'
}
notification = {
     'delete': {'command': 'notification:delete', 'desc': 'Delete a generated admin notification for the given user', 'path': ['notification', 'delete']},
     'generate': {'command': 'notification:generate', 'desc': 'Generate a notification for the given user', 'path': ['notification', 'generate']},
     'test-push': {'command': 'notification:test-push', 'desc': ' Generate a notification for the given user', 'path': ['notification', 'test-push']},
     'occ_lib_name':'notification'
}
photos = {
         'albums':{
                 'add': {'command': 'photos:albums:add', 'desc': 'Add specified photo to album', 'path': ['photos', 'albums', 'add']},
                 'create': {'command': 'photos:albums:create', 'desc': ' Create a new album for a user', 'path': ['photos', 'albums', 'create']},
        },
         'update-1000-cities': {'command': 'photos:update-1000-cities', 'desc': 'Update the list of 1000 and more inhabitant cities', 'path': ['photos', 'update-1000-cities']},
     'occ_lib_name':'photos'
}
preview = {
         'cleanup': {'command': 'preview:cleanup', 'desc': 'Removes existing preview files', 'path': ['preview', 'cleanup']},
         'generate': {'command': 'preview:generate', 'desc': ' generate a preview for a file', 'path': ['preview', 'generate']},
         'repair': {'command': 'preview:repair', 'desc': ' distributes the existing previews into subfolders', 'path': ['preview', 'repair']},
         'reset-rendered-texts': {'command': 'preview:reset-rendered-texts', 'desc': ' Deletes all generated avatars and previews of text and md files', 'path': ['preview', 'reset-rendered-texts']},
     'occ_lib_name':'preview'
}
router = {
         'list': {'command': 'router:list', 'desc': 'Find the target of a route or all routes of an app', 'path': ['router', 'list']},
         'match': {'command': 'router:match', 'desc': ' Match a URL to the target route', 'path': ['router', 'match']},
     'occ_lib_name':'router'
}
security = {
         'bruteforce':{
                 'attempts': {'command': 'security:bruteforce:attempts', 'desc': ' Show bruteforce attempts status for a given IP address', 'path': ['security', 'bruteforce', 'attempts']},
                 'reset': {'command': 'security:bruteforce:reset', 'desc': 'resets bruteforce attempts for given IP address', 'path': ['security', 'bruteforce', 'reset']},
        },
         'certificates':{
                 'security:certificates': {'command': 'security:certificates', 'desc': 'list trusted certificates', 'path': ['security', 'certificates'], 'export': {'command': 'security:certificates:export', 'desc': ' export the certificate bundle', 'path': ['security', 'certificates', 'export']}, 'import': {'command': 'security:certificates:import', 'desc': ' import trusted certificate in PEM format', 'path': ['security', 'certificates', 'import']}, 'remove': {'command': 'security:certificates:remove', 'desc': ' remove trusted certificate', 'path': ['security', 'certificates', 'remove']}},
        },
     'occ_lib_name':'security'
}
serverinfo = {
         'update-storage-statistics': {'command': 'serverinfo:update-storage-statistics', 'desc': ' Triggers an update of the counts related to storages used in serverinfo', 'path': ['serverinfo', 'update-storage-statistics']},
     'occ_lib_name':'serverinfo'
}
share = {
         'list': {'command': 'share:list', 'desc': ' List available shares', 'path': ['share', 'list']},
     'occ_lib_name':'share'
}
sharing = {
         'cleanup-remote-storages': {'command': 'sharing:cleanup-remote-storages', 'desc': 'Cleanup shared storage entries that have no matching entry in the sharesexternal table', 'path': ['sharing', 'cleanup-remote-storages']},
         'delete-orphan-shares': {'command': 'sharing:delete-orphan-shares', 'desc': ' Delete shares where the owner no longer has access to the file', 'path': ['sharing', 'delete-orphan-shares']},
         'expiration-notification': {'command': 'sharing:expiration-notification', 'desc': 'Notify share initiators when a share will expire the next day', 'path': ['sharing', 'expiration-notification']},
         'fix-share-owners': {'command': 'sharing:fix-share-owners', 'desc': ' Fix owner of broken shares after transfer ownership on old versions', 'path': ['sharing', 'fix-share-owners']},
     'occ_lib_name':'sharing'
}
support = {
         'report': {'command': 'support:report', 'desc': ' Generate a system report', 'path': ['support', 'report']},
     'occ_lib_name':'support'
}
tables = {
         'add': {'command': 'tables:add', 'desc': ' Add a table', 'path': ['tables', 'add']},
         'clean': {'command': 'tables:clean', 'desc': ' Clean the tables data', 'path': ['tables', 'clean']},
         'contexts':{
                 'list': {'command': 'tables:contexts:list', 'desc': ' Get all contexts or contexts available to a specified user', 'path': ['tables', 'contexts', 'list']},
                 'show': {'command': 'tables:contexts:show', 'desc': ' Get all contexts or contexts available to a specified user', 'path': ['tables', 'contexts', 'show']},
        },
         'legacy':{
                 'clean': {'command': 'tables:legacy:clean', 'desc': 'Clean the tables legacy data', 'path': ['tables', 'legacy', 'clean']},
                 'transfer':{
                         'rows': {'command': 'tables:legacy:transfer:rows', 'desc': 'Transfer table legacy rows to new schema', 'path': ['tables', 'legacy', 'transfer', 'rows']},
                },
        },
         'list': {'command': 'tables:list', 'desc': 'List all tables', 'path': ['tables', 'list']},
         'owner': {'command': 'tables:owner', 'desc': ' Set new owner for a table', 'path': ['tables', 'owner']},
         'remove': {'command': 'tables:remove', 'desc': 'Remove a table', 'path': ['tables', 'remove']},
         'update': {'command': 'tables:update', 'desc': 'tablesrename Rename a table', 'path': ['tables', 'update']},
     'occ_lib_name':'tables'
}
tag = {
         'add': {'command': 'tag:add', 'desc': 'Add new tag', 'path': ['tag', 'add']},
         'delete': {'command': 'tag:delete', 'desc': ' delete a tag', 'path': ['tag', 'delete']},
         'edit': {'command': 'tag:edit', 'desc': ' edit tag attributes', 'path': ['tag', 'edit']},
         'files':{
                 'add': {'command': 'tag:files:add', 'desc': 'Add a systemtag to a file or folder', 'path': ['tag', 'files', 'add']},
                 'delete': {'command': 'tag:files:delete', 'desc': ' Delete a systemtag from a file or folder', 'path': ['tag', 'files', 'delete']},
                 'delete-all': {'command': 'tag:files:delete-all', 'desc': ' Delete all systemtags from a file or folder', 'path': ['tag', 'files', 'delete-all']},
        },
         'list': {'command': 'tag:list', 'desc': ' list tags', 'path': ['tag', 'list']},
     'occ_lib_name':'tag'
}
talk = {
         'active-calls': {'command': 'talk:active-calls', 'desc': 'Allows you to check if calls are currently in process', 'path': ['talk', 'active-calls']},
         'bot':{
                 'create': {'command': 'talk:bot:create', 'desc': 'Creates a new bot on the server with response feature only', 'path': ['talk', 'bot', 'create']},
                 'install': {'command': 'talk:bot:install', 'desc': ' Install a new bot on the server', 'path': ['talk', 'bot', 'install']},
                 'list': {'command': 'talk:bot:list', 'desc': 'List all installed bots of the server or a conversation', 'path': ['talk', 'bot', 'list']},
                 'remove': {'command': 'talk:bot:remove', 'desc': 'Remove a bot from a conversation', 'path': ['talk', 'bot', 'remove']},
                 'setup': {'command': 'talk:bot:setup', 'desc': ' Add a bot to a conversation', 'path': ['talk', 'bot', 'setup']},
                 'state': {'command': 'talk:bot:state', 'desc': ' Change the state or feature list for a bot', 'path': ['talk', 'bot', 'state']},
                 'uninstall': {'command': 'talk:bot:uninstall', 'desc': ' Uninstall a bot from the server', 'path': ['talk', 'bot', 'uninstall']},
        },
         'monitor':{
                 'calls': {'command': 'talk:monitor:calls', 'desc': ' Prints a list with conversations that have an active call as well as their participant count', 'path': ['talk', 'monitor', 'calls']},
                 'room': {'command': 'talk:monitor:room', 'desc': 'Prints the number of attendees active sessions and participant in the call', 'path': ['talk', 'monitor', 'room']},
        },
         'phone-number':{
                 'add': {'command': 'talk:phone-number:add', 'desc': 'Add a mapping entry to map a phone number to an user', 'path': ['talk', 'phone-number', 'add']},
                 'find': {'command': 'talk:phone-number:find', 'desc': ' Find a phone number or the phone number of an user', 'path': ['talk', 'phone-number', 'find']},
                 'import': {'command': 'talk:phone-number:import', 'desc': ' Import a CSV list format numberuser for SIP dialin', 'path': ['talk', 'phone-number', 'import']},
                 'remove': {'command': 'talk:phone-number:remove', 'desc': ' Remove a mapping entry by phone number', 'path': ['talk', 'phone-number', 'remove']},
                 'remove-user': {'command': 'talk:phone-number:remove-user', 'desc': 'Remove mapping entries by user', 'path': ['talk', 'phone-number', 'remove-user']},
        },
         'recording':{
                 'consent': {'command': 'talk:recording:consent', 'desc': ' List all matching consent that were given to be audio and video recorded during a call requires administrator or moderator configuration', 'path': ['talk', 'recording', 'consent']},
        },
         'room':{
                 'add': {'command': 'talk:room:add', 'desc': 'Adds users to a room', 'path': ['talk', 'room', 'add']},
                 'create': {'command': 'talk:room:create', 'desc': ' Create a new room', 'path': ['talk', 'room', 'create']},
                 'delete': {'command': 'talk:room:delete', 'desc': ' Deletes a room', 'path': ['talk', 'room', 'delete']},
                 'demote': {'command': 'talk:room:demote', 'desc': ' Demotes participants of a room to regular users', 'path': ['talk', 'room', 'demote']},
                 'promote': {'command': 'talk:room:promote', 'desc': 'Promotes participants of a room to moderators', 'path': ['talk', 'room', 'promote']},
                 'remove': {'command': 'talk:room:remove', 'desc': ' Remove users from a room', 'path': ['talk', 'room', 'remove']},
                 'update': {'command': 'talk:room:update', 'desc': ' Updates a room', 'path': ['talk', 'room', 'update']},
        },
         'signaling':{
                 'add': {'command': 'talk:signaling:add', 'desc': ' Add an external signaling server', 'path': ['talk', 'signaling', 'add']},
                 'delete': {'command': 'talk:signaling:delete', 'desc': 'Remove an existing signaling server', 'path': ['talk', 'signaling', 'delete']},
                 'list': {'command': 'talk:signaling:list', 'desc': 'List external signaling servers', 'path': ['talk', 'signaling', 'list']},
                 'verify-keys': {'command': 'talk:signaling:verify-keys', 'desc': ' Verify if the stored public key matches the stored private key for the signaling server', 'path': ['talk', 'signaling', 'verify-keys']},
        },
         'stun':{
                 'add': {'command': 'talk:stun:add', 'desc': 'Add a new STUN server', 'path': ['talk', 'stun', 'add']},
                 'delete': {'command': 'talk:stun:delete', 'desc': ' Remove an existing STUN server', 'path': ['talk', 'stun', 'delete']},
                 'list': {'command': 'talk:stun:list', 'desc': ' List STUN servers', 'path': ['talk', 'stun', 'list']},
        },
         'turn':{
                 'add': {'command': 'talk:turn:add', 'desc': 'Add a TURN server', 'path': ['talk', 'turn', 'add']},
                 'delete': {'command': 'talk:turn:delete', 'desc': ' Remove an existing TURN server', 'path': ['talk', 'turn', 'delete']},
                 'list': {'command': 'talk:turn:list', 'desc': ' List TURN servers', 'path': ['talk', 'turn', 'list']},
        },
         'user':{
                 'remove': {'command': 'talk:user:remove', 'desc': ' Remove a user from all their rooms', 'path': ['talk', 'user', 'remove']},
                 'transfer-ownership': {'command': 'talk:user:transfer-ownership', 'desc': ' Adds the destinationuser with the same participant type to all not onetoone conversations of sourceuser', 'path': ['talk', 'user', 'transfer-ownership']},
        },
     'occ_lib_name':'talk'
}
taskprocessing = {
         'task-type':{
                 'set-enabled': {'command': 'taskprocessing:task-type:set-enabled', 'desc': ' Enable or disable a task type', 'path': ['taskprocessing', 'task-type', 'set-enabled']},
        },
         'task':{
                 'cleanup': {'command': 'taskprocessing:task:cleanup', 'desc': 'cleanup old tasks', 'path': ['taskprocessing', 'task', 'cleanup']},
                 'get': {'command': 'taskprocessing:task:get', 'desc': 'Display all information for a specific task', 'path': ['taskprocessing', 'task', 'get']},
                 'list': {'command': 'taskprocessing:task:list', 'desc': ' list tasks', 'path': ['taskprocessing', 'task', 'list']},
                 'stats': {'command': 'taskprocessing:task:stats', 'desc': 'get statistics for tasks', 'path': ['taskprocessing', 'task', 'stats']},
        },
     'occ_lib_name':'taskprocessing'
}
text = {
         'reset': {'command': 'text:reset', 'desc': ' Reset a text document session to the current file content', 'path': ['text', 'reset']},
     'occ_lib_name':'text'
}
theming = {
         'config': {'command': 'theming:config', 'desc': ' Set theming app config values', 'path': ['theming', 'config']},
     'occ_lib_name':'theming'
}
trashbin = {
         'cleanup': {'command': 'trashbin:cleanup', 'desc': ' Remove deleted files', 'path': ['trashbin', 'cleanup']},
         'expire': {'command': 'trashbin:expire', 'desc': 'Expires the users trashbin', 'path': ['trashbin', 'expire']},
         'restore': {'command': 'trashbin:restore', 'desc': ' Restore all deleted files according to the given filters', 'path': ['trashbin', 'restore']},
         'size': {'command': 'trashbin:size', 'desc': 'Configure the target trashbin size', 'path': ['trashbin', 'size']},
     'occ_lib_name':'trashbin'
}
twofactorauth = {
         'cleanup': {'command': 'twofactorauth:cleanup', 'desc': 'Clean up the twofactor userprovider association of an uninstalledremoved provider', 'path': ['twofactorauth', 'cleanup']},
         'disable': {'command': 'twofactorauth:disable', 'desc': 'Disable twofactor authentication for a user', 'path': ['twofactorauth', 'disable']},
         'enable': {'command': 'twofactorauth:enable', 'desc': ' Enable twofactor authentication for a user', 'path': ['twofactorauth', 'enable']},
         'enforce': {'command': 'twofactorauth:enforce', 'desc': 'Enableddisable enforced twofactor authentication', 'path': ['twofactorauth', 'enforce']},
         'state': {'command': 'twofactorauth:state', 'desc': 'Get the twofactor authentication 2FA state of a user', 'path': ['twofactorauth', 'state']},
     'occ_lib_name':'twofactorauth'
}
update = {
         'check': {'command': 'update:check', 'desc': ' Check for server and app updates', 'path': ['update', 'check']},
     'occ_lib_name':'update'
}
user = {
         'add': {'command': 'user:add', 'desc': ' adds an account', 'path': ['user', 'add']},
         'auth-tokens':{
                 'add': {'command': 'user:auth-tokens:add', 'desc': ' useraddapppassword Add app password for the named account', 'path': ['user', 'auth-tokens', 'add']},
                 'delete': {'command': 'user:auth-tokens:delete', 'desc': 'Deletes an authentication token', 'path': ['user', 'auth-tokens', 'delete']},
                 'list': {'command': 'user:auth-tokens:list', 'desc': 'List authentication tokens of an user', 'path': ['user', 'auth-tokens', 'list']},
        },
         'clear-avatar-cache': {'command': 'user:clear-avatar-cache', 'desc': 'clear avatar cache', 'path': ['user', 'clear-avatar-cache']},
         'delete': {'command': 'user:delete', 'desc': 'deletes the specified user', 'path': ['user', 'delete']},
         'disable': {'command': 'user:disable', 'desc': ' disables the specified user', 'path': ['user', 'disable']},
         'enable': {'command': 'user:enable', 'desc': 'enables the specified user', 'path': ['user', 'enable']},
         'info': {'command': 'user:info', 'desc': 'show user info', 'path': ['user', 'info']},
         'keys':{
                 'verify': {'command': 'user:keys:verify', 'desc': ' Verify if the stored public key matches the stored private key', 'path': ['user', 'keys', 'verify']},
        },
         'lastseen': {'command': 'user:lastseen', 'desc': 'shows when the user was logged in last time', 'path': ['user', 'lastseen']},
         'list': {'command': 'user:list', 'desc': 'list configured users', 'path': ['user', 'list']},
         'profile': {'command': 'user:profile', 'desc': ' Read and modify user profile properties', 'path': ['user', 'profile']},
         'report': {'command': 'user:report', 'desc': 'shows how many users have access', 'path': ['user', 'report']},
         'resetpassword': {'command': 'user:resetpassword', 'desc': ' Resets the password of the named user', 'path': ['user', 'resetpassword']},
         'setting': {'command': 'user:setting', 'desc': ' Read and modify user settings', 'path': ['user', 'setting']},
         'sync-account-data': {'command': 'user:sync-account-data', 'desc': ' sync user backend data to accounts table for configured users', 'path': ['user', 'sync-account-data']},
         'welcome': {'command': 'user:welcome', 'desc': ' Sends the welcome email', 'path': ['user', 'welcome']},
     'occ_lib_name':'user'
}
versions = {
         'cleanup': {'command': 'versions:cleanup', 'desc': ' Delete versions', 'path': ['versions', 'cleanup']},
         'expire': {'command': 'versions:expire', 'desc': 'Expires the users file versions', 'path': ['versions', 'expire']},
     'occ_lib_name':'versions'
}
webhooklisteners = {
         'list': {'command': 'webhook_listeners:list', 'desc': ' Lists configured webhook listeners', 'path': ['webhook_listeners', 'list']},
     'occ_lib_name':'webhooklisteners'
}
workflows = {
         'list': {'command': 'workflows:list', 'desc': ' Lists configured workflows', 'path': ['workflows', 'list']},
     'occ_lib_name':'workflows'
}
members_occ_lib = ['common', 'activity', 'admindelegation', 'app', 'appapi', 'background', 'backgroundjob', 'bookmarks', 'broadcast', 'calendar', 'circles', 'config', 'dav', 'db', 'encryption', 'federation', 'files', 'group', 'info', 'integrity', 'l10n', 'log', 'maintenance', 'memcache', 'metadata', 'migrations', 'notification', 'photos', 'preview', 'router', 'security', 'serverinfo', 'share', 'sharing', 'support', 'tables', 'tag', 'talk', 'taskprocessing', 'text', 'theming', 'trashbin', 'twofactorauth', 'update', 'user', 'versions', 'webhooklisteners', 'workflows']