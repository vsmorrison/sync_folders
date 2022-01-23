import dirsync


def sync_folders(source, replica, log):
    dirsync.sync(source, replica, 'sync', purge=True, logger=log)
