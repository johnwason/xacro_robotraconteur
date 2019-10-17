xacro-robotraconteur is a modified version of ROS xacro. See http://wiki.ros.org/xacro for more information.

This modified xacro does not use ros packages, and instead uses Robot Raconteur "buckets" which are essentially just directories, archives, or some other type of resource storage. Buckets are identified with a name and/or a UUID. Currently this version only works with directories and named buckets.

To specify the buckets, the environmental variable `ROBOTRACONTEUR_BUCKET_FILES` must point to a list of `bucket.yml` files. These `bucket.yml` files contain the names and directories of the buckets. An example `bucket.yml`:

    buckets:
      - name: sawyer_description
        directory: C:\rosws\src\sawyer_robot\sawyer_description
      - name: sawyer_moveit_config
        directory: C:\rosws\src\sawyer_moveit\sawyer_moveit_config