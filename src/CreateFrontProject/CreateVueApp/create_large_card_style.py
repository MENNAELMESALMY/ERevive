def create_large_card_style(route):
    f = open(route, 'w') 
    f.write('''
.main_cards{
  display: flex;
  flex-direction: column;
  width: 90%;
  background-color: #fff;
  padding: 20px;
  margin: auto;
}
.big_card{
  display: flex;
  flex-wrap: wrap;
  margin: 20px;
  box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
  padding: 10px;
}
.attribute{
    padding: 10px;
    margin: 3px;
    border: 1px solid rgba(175, 175, 175, 0.889);
    transition-duration: 0.4s;
}
.attribute:hover {
    box-shadow: 0 5px 15px rgb(168, 167, 167);
}

    ''')
    f.close()
