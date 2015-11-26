## easyui 用到的翻页代码 ##

```go
  func (w *AdminApiUserController) GetUser() {
    //url中的就要带冒号获取
    //如果是POST过来的数据，就不用
    role := w.GetString(":role")
    page, _ := w.GetInt("page", 0)
    rows, _ := w.GetInt("rows", 0)
    sort := w.GetString("sort")
    order := w.GetString("order")

    loginName := w.GetString("LoginName")
    userRole, _ := w.GetInt("UserRole", 0)
    userStatus, _ := w.GetInt("UserStatus", 0)
    beego.Debug("loginName", loginName)
    beego.Debug("userRole", userRole)
    beego.Debug("userStatus", userStatus)

    if role == "sys" {
      wd, wdcount, err := models.GetUserByRole(loginName, userRole, userStatus, page, rows, sort, order)
      if err != nil {
        w.Data["json"] = err.Error()
      } else if wdcount == 0 {
        w.Data["json"] = &map[string]interface{}{"total": wdcount, "rows": ""}
      } else {
        w.Data["json"] = &map[string]interface{}{"total": wdcount, "rows": &wd}
      }
    } else {
      w.Data["json"] = "请输入用户类型。"
    }

    w.ServeJson()
  }

  //根据账户类别获取用户信息列表
  func GetUserByRole(loginname string, userrole int, userstatus int, page int, rows int, sort string, order string) (users []*Tusers, total int64, err error) {
    user := new(Tusers)

    if len(loginname) > 0 {
      user.User_login = loginname
    }
    if userrole != 0 {
      user.User_role = userrole
    }
    if userstatus != 0 {
      user.User_status = userstatus
    }

    total, err = Engine.Count(user)
    if err != nil {
      return nil, 0, errors.New(err.Error())
    }
    beego.Debug("sort", sort)
    if total > 0 && rows > 0 && page > 0 {
      engine := Engine.Desc(sort)
      if order == "asc" {
        engine = Engine.Asc(sort)
      }
      userrows, err := engine.Limit(rows, (page-1)*rows).Rows(user)
      if err != nil {
        return nil, 0, errors.New(err.Error())
      }
      defer userrows.Close()
      for userrows.Next() {
        user = new(Tusers)
        err = userrows.Scan(user)
        users = append(users, user)
      }
    }
    return users, total, err
  }
