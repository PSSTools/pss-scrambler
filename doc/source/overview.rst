######################
PSS Scrambler Overview
######################

It is often useful to share proprietary verification code with a tool vendor
as a testcase for a bug. In these cases, it is desirable to have the testcase
code function normally, but not contain any hints as to its purpose. 

Enter the Obfuscator. The task of an obfuscator is to transform identifiers
within the source to obscure the true purpose and application of the code,
while not altering its functionality.

PSS Scrambler is an obfuscation tool for Accellera Portable Test and Stimulus (PSS).
It accepts a list of PSS files, transforms non-reserved identifiers within them,
producing a single output file.

Here's a quick example:

.. code-block:: 
   :caption: Input Source

    /**
     * 
     */
    component my_c {
        action A {
        }
    }

    component my2_c {
        my_c  c1;
        my_c  c2;
        my_c  c3;
        my_c  c4;

        action Entry {
            do my_c::A;
        }
    }

The result after processing with PSS Scrambler is shown below. Note a few things:

- Comments are stripped by default. They can be preserved.
- User-specified identifiers are replaced with other English-language words of 
  similar length
- Special identifier suffixes (eg _c to denote a component type) are preserved


.. code-block:: 
   :caption: Output Source

    component phys_c {
        action c {
        }
    }

    component guide_c {
        phys_c  lc;
        phys_c  fl;
        phys_c  bp;
        phys_c  cn;

        action armor {
            do phys_c::c;
        }
    }

Installing PSS Scrambler
========================

PSS Scrambler is most easily installed via `pip`. Simply use the command below:

.. code-block::

    % python3 -m pip install --upgrade pss-scrambler


Once installed, PSS scrambler can be invoked via the Python module or wrapper script:

.. code-block::
    
    % python3 -m pss_scrambler ...
    % pss-scrambler ...


