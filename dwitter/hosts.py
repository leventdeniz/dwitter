from django_hosts import patterns, host

host_patterns = patterns(
    '',
    host(r'www', 'dwitter.urls', name='www'),
    host(r'dweet', 'dwitter.dweet.urls', name='dweet'),
)
