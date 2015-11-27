 ## WordPress数据库表及字段详解 ##

> 1.wp_posts表，存储文章信息，如文章标题、正文、摘要、作者、发布时间、访问密码、评论数、修改时间、文章地址（非静态化之前的，带？和数字ID）等；

```sql
	SELECT ID,  --bigint(20)自增长ID
	post_author, --bigint(20)对应作者ID
	post_date,   --datetime发布时间
	post_date_gmt, --datetime发布时间（GMT+0时间）
	post_content,  --longtext正文
	post_title,    --text标题
	post_excerpt,  --text摘录
	post_status,   --varchar(20)文章状态（'draft' | 'publish' | 'pending'| 'future' | 'private'）
	comment_status,  --varchar(20)评论状态（open/closed关闭评论）
	ping_status,     --varchar(20)PING状态（open/closed关闭 pingbacks和trackbacks）
	post_password,   --varchar(20)文章密码
	post_name,       --varchar(200)文章缩略名
	to_ping,         --text该文章需要ping到的地址
	pinged,          --text已经PING过的链接
	post_modified,   --datetime修改时间
	post_modified_gmt, --datetime修改时间（GMT+0时间）
	post_content_filtered, --longtext未知
	post_parent,           --bigint(20)父文章，主要用于PAGE
	guid,                  --varchar(255)未知 (post:/wordpress/?p=1),(page:/wordpress/?page_id=2)这里面的ID为自增长ID
	menu_order,            --int(11)如果新文章是页面，设置显示顺序
	post_type,             --varchar(20)文章类型'post' | 'page' | 'link' | 'nav_menu_item' | custom post type；文章类型：文章、页面、链接、菜单、其他定制类型
	post_mime_type,        --varchar(100)MIME类型
	comment_count          --bigint(20)评论总数
	FROM wordpress . wp_posts;
```

 > 2.wp_comments表，存储评论信息，如评论内容、评论所属文章、评论人昵称、邮箱、URL等；

```sql
	SELECT comment_ID,          --bigint(20)自增唯一ID
	comment_post_ID,     --bigint(20)对应文章ID
	comment_author,      --tinytext评论者
	comment_author_email,                        --varchar(100)评论者邮箱
	comment_author_url,                          --varchar(200)评论者网址
	comment_author_IP,                           --varchar(100)评论者IP
	comment_date,                                --datetime评论时间
	comment_date_gmt,                            --datetime评论时间（GMT+0时间）
	comment_content,                             --text评论正文
	comment_karma,                               --int(11)
	comment_approved,                            --varchar(20)评论是否被批准（0拒绝/1批准）
	comment_agent,                               --varchar(255)评论者的USER AGENT
	comment_type,                                --varchar(20)评论类型(pingback/普通)
	comment_parent,                              --bigint(20)父评论ID
	user_id                                      --bigint(20)评论者用户ID（不一定存在）
	FROM wordpress . wp_comments
```