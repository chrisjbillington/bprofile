# bprofile

A wrapper around profile/cProfile, gprof2dot and dot,
providing a simple context manager for profiling sections
of Python code and producing visual graphs of profiling results.

(
[view on pypi](https://pypi.python.org/pypi/bprofile/);
[view on Bitbucket](https://bitbucket.org/cbillington/bprofile)
)

   * Install with `python setup.py install` 
   * Install the latest release version using `pip install bprofile` or `easy_install bprofile`
   * Requires Graphviz to be installed (gprof2dot is bundled)
   * Compatible with Windows and *nix
   
This package provides a single class:

##`BProfile(output_path, threshold_percent=2.5, report_interval=5)`
    
A profiling context manager. Outputs a .png graph made via profile/cProfile, gprof2dot
and graphviz. graphviz is the only external dependency.


### Example usage:

```
#!python
profiler = BProfile('output.png')

with profiler:
    do_some_stuff()

do_some_stuff_that_wont_be_profiled()

with profiler:
    do_some_more_stuff()
```


### Arguments:

    - output_path:       The name of the .png report file you would like to output.
                        '.png' will be appended if not present.

    - threshold_percent: `int` or `float` for the minimum percentage of total cumulative
                         time a call should have to be included in the output.
                         Defaults to 2.5.

    - report_interval:   The minimum time in between output file generation. This is to
                         minimise overhead on your program, (even though this overhead
                         will only be incurred when no code is being profiled), while
                         allowing you to have ongoing results of the profiling
                         while your code is still running. Defaults to 5 (seconds).


### Output generation

The profiler will return immediately after the context manager, and will
generate its `.png` report in a separate thread. If the same context
manager is used multiple times output will be generated at most every
`report_interval` seconds (default: 5). The delay is to allow blocks to
execute many times in between reports, rather than slowing your
program down with generating graphs all the time. This means that if your
profile block is running repeatedly, a new report will be produced every
`report_interval` seconds.

Pending reports will be generated at interpreter shutdown.

Note that even if `report_interval` is short, reporting will not interfere with the
profiling results themselves, as a lock is acquired that will prevent profiled
code from running at the same time as the report generation code. So the
overhead produced by report generation does not affect the results of
profiling - this overhead will only affect portions of your code that are not
being profiled.

The lock is shared between instances, and so you can freely instantiate many
Profile objects to profile different parts of your code. Instances with the same
output file name will share an underlying profile/cProfile profiler, and so their
reports will be combined. Profile objects are thread safe, however, so a single instance
can be shared as well anywhere in your program.

Note that since only one profiler can be running at a time, two profiled
pieces of code waiting on each other in any way will deadlock, regardless of
whether they share an underlying profile/cProfile profiler or not.

### Public methods

##`do_report()`

Collect statistics and output a .png file of the profiling report.

This occurs automatically at a rate of report_interval, but one can
call this method to report results sooner. The report will include
results from all BProfile instances that have the same output
filepath, and no more automatic reports (if further profiling is done)
will be produced until after the minimum delay_interval of those
instances.

This method can be called at any time and is threadsafe, but it will
acquire the class lock and so will block until any profiling in other
threads is complete. The lock is re-entrant, so this method can be
called during profiling in the current thread. This is not advisable
however, as the overhead incorred will skew profiling results.
