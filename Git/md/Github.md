- `git clone xxURL` 从GitHub上copy需要clone的url下载到本地
- `git config --get remote.origin.url` 查看GitHub的url
- `git add xxfile` 把xxfile更新到缓存区
- `git commit -m “some messages”` 确认所有更新
- `git add --all && git commit -m "comment"`更新缓存一次性完成，包括所有文件
- `git checkout branch_name` 转到xxbranch上
- `git push --set-upstream origin branch_name`  push the current local branch to the remote repository (origin) and set it as the upstream branch
- `git fetch + git merge = git pull`
- `git merge branch_name` 把xxbranch和main的内容合并
- `git log` 显示commit的数量和内容 q退出
- `git branch -d branch_name` 删掉本地branch, 如果要强制删除就`git branch -D branch_name`
- `git push origin --delete branch_name`删除远程branch
- `git push origin main branch_name` 把main的commit推送到remote上的branch