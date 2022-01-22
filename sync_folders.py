import dirsync


def sync_folders(source, replica):
    synchronization = dirsync.sync(source, replica)
