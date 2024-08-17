# just an example of using a function generator with the yield keyword to create a dependency
#  https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do-in-python
# Probably not going to need this technique for creating dependencies unless creating library level code
#  https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/#dependencies-with-yield-and-httpexception
async def get_db():
    db = DBSession()
    try:
        yield db
    finally:
        db.close()


from typing import Annotated

from fastapi import Depends


async def dependency_a():
    dep_a = generate_dep_a()
    try:
        yield dep_a
    finally:
        dep_a.close()


async def dependency_b(dep_a: Annotated[DepA, Depends(dependency_a)]):
    dep_b = generate_dep_b()
    try:
        yield dep_b
    finally:
        dep_b.close(dep_a)


async def dependency_c(dep_b: Annotated[DepB, Depends(dependency_b)]):
    dep_c = generate_dep_c()
    try:
        yield dep_c
    finally:
        dep_c.close(dep_b)
