Step 1: From your project repository, bring in the changes and test.

git fetch origin
git checkout -b sm-slam origin/sm-slam
git merge main

Step 2: Merge the changes and update on GitHub.

git checkout main
git merge --no-ff sm-slam
git push origin main