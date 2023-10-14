| git command | zsh alias | action |
| ---|---|---|
| git add * | gaa | stages all changes|
| git commit -m"message"| gc -m"message"| Commits staged changes|
| git pull | gl | pulls any changes from remote repo|
| git push | gp | pushes changes in local repo to remote|
| git checkout \<commit> | gco \<commit> | Changes the files to how it was at that specific commit |

You can find where the zsh git aliases are stored on your computer in: `~/.oh-my-zsh/plugins/git.plugin.zsh`

Note: you can define your own aliases in `~/.zshrc`