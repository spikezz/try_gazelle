load("@bazel_gazelle//:def.bzl", "gazelle")

# Our gazelle target points to the python gazelle binary.
# This is the simple case where we only need one language supported.
# If you also had proto, go, or other gazelle-supported languages,
# you would also need a gazelle_binary rule.
# See https://github.com/bazelbuild/bazel-gazelle/blob/master/extend.rst#example
gazelle(
    name = "gazelle",
    gazelle = "@rules_python_gazelle_plugin//python:gazelle_binary",
)

filegroup(
    name = "requirements_lock",
    srcs = ["requirements_lock.txt"],
    visibility = ["//visibility:public"],
)
