import LinodeFS

def main():
    usage="""
LinodeFS

""" + fuse.Fuse.fusage
    server = LinodeFS(version="%prog " + fuse.__version__,
                     usage=usage,
                     dash_s_do='setsingle')

    server.parser.add_option(mountopt='api_key', metavar='API_KEY',
            help=("API Key"))
    server.parser.add_option(mountopt='api_url', metavar='API_URL',
            help=("API URL"))
    server.parse(values=server, errex=1)

    if not (hasattr(server, 'api_key')):
        print >>sys.stderr, "Please specify an API Key."
        sys.exit(1)

    try:
        server.make_connection()
    except Exception, err:
        print >>sys.stderr, "Cannot connect to Linode API: %s" % str(err)
        sys.exit(1)

    server.main()
