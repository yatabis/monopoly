var nPlayers = 0;
var players_name = ['プレイヤーを選択', "", "", "", "", "", ""];
var players_money = [2000000, 0, 0, 0, 0, 0, 0];
var plus_player_id = 0;
var minus_player_id = 0;

function resetBody() {
  let body = document.querySelector('body');
  while (body.firstChild) body.removeChild(body.firstChild);
}

function setPageTitle(text) {
  let title = document.createElement('h1');
  title.textContent = text;
  document.querySelector('body').appendChild(title);
}

function setPlayersNumberView() {
  resetBody();
  setPageTitle("プレイ人数を選ぶ");
  let body = document.querySelector('body');
  for (let i = 2; i <= 6; i++) {
    let div = document.createElement('div');
    div.setAttribute('class', 'player-number');
    div.setAttribute('onclick', 'setPlayersNameView(' + i + ')');
    div.innerText = i + "人でプレイ";
    body.appendChild(div);
  }
}

function setPlayersNameView(p) {
  nPlayers = p;
  resetBody();
  setPageTitle("プレイヤーを決める");
  let body = document.querySelector('body');
  for (let i = 1; i <= nPlayers; i++) {
    let player = document.createElement('input');
    player.setAttribute('id', 'player' + i);
    player.setAttribute('class', 'player-name');
    player.setAttribute('value', players_name[i]);
    player.setAttribute('placeholder', 'player' + i);
    body.appendChild(player);
    body.appendChild(document.createElement('br'));
  }
  let submit = document.createElement('div');
  submit.setAttribute('id', 'submit');
  submit.innerText = "プレイスタート";
  submit.setAttribute('onclick', 'setStart()');
  body.appendChild(submit);
  let back = document.createElement('div');
  back.setAttribute('id', 'back');
  back.setAttribute('onclick', 'setPlayersNumberView()');
  back.innerText = "人数選択に戻る";
  body.appendChild(back);
}

function setStart() {
  for (let i = 1; i<= nPlayers; i++) {
    players_name[i] = document.getElementById('player' + i).value;
  }
  resetBody();
  setMemoryBankView();
  setPlayerList('plus-player');
  setPlayerList('minus-player');
}

function setMemoryBankView() {
  let bank = document.createElement('div');
  bank.setAttribute('id', 'memory-bank');
  document.querySelector('body').appendChild(bank);

  let plus = document.createElement('select');
  plus.setAttribute('id', 'plus-player');
  plus.setAttribute('size', nPlayers);
  plus.setAttribute('onChange', "selectPlayer('plus')");
  bank.appendChild(plus);

  let minus = document.createElement('select');
  minus.setAttribute('id', 'minus-player');
  minus.setAttribute('size', nPlayers);
  minus.setAttribute('onChange', "selectPlayer('minus')");
  bank.appendChild(minus);

  bank.appendChild(plus);
  setBankKey('arrow', 'circle', '←');
  setBankKey('M', 'rect', 'M');
  setBankKey('K', 'rect', 'K');
  setBankKey('key1', 'square', '1');
  setBankKey('key2', 'square', '2');
  setBankKey('key3', 'square', '3');
  setBankKey('key4', 'square', '4');
  setBankKey('key5', 'square', '5');
  setBankKey('key6', 'square', '6');
  setBankKey('key7', 'square', '7');
  setBankKey('key8', 'square', '8');
  setBankKey('key9', 'square', '9');
  setBankKey('key0', 'square', '0');
  setBankKey('dot', 'square', '.');
  setBankKey('clear', 'circle', 'C');
  setBankKey('display-main', '', '0');
  setBankKey('display-plus', '', '0');
  setBankKey('display-minus', '', '0');
}

function setBankKey(id, cls, text) {
  let key = document.createElement('div');
  key.setAttribute('id', id);
  key.setAttribute('class', cls);
  key.setAttribute('onclick', "pressKey('"+ id + "')");
  key.innerText = text;
  document.getElementById('memory-bank').appendChild(key);
}

function setPlayerList(id) {
  let select = document.getElementById(id);
  for (let i = 0; i <= nPlayers; i++) {
    let option = document.createElement('option');
    option.setAttribute('value', players_name[i]);
    option.setAttribute('label', players_name[i]);
    option.innerText = players_name[i];
    select.appendChild(option);
  }
}

function selectPlayer(pm) {
  let player_id = document.getElementById(pm + '-player').selectedIndex;
  if (pm === 'plus') {
    plus_player_id = player_id;
    if (player_id !== 0) {
      document.getElementById('display-plus').innerText = players_money[player_id];
    } else {
      document.getElementById('display-plus').innerText = '0';
    }
  } else if (pm === 'minus') {
    minus_player_id = player_id;
    if (player_id !== 0) {
      document.getElementById('display-minus').innerText = players_money[player_id];
    } else {
      document.getElementById('display-plus').innerText = '0';
    }
  }
}

function pressKey(key) {
  let display = document.getElementById('display-main');
  if (key === 'clear') {
    display.innerText = '0';
  } else if (key === 'M') {
    updateMoney(parseInt(parseFloat(display.innerText) * 1000000));
    display.innerText = '0';
  } else if (key === 'K') {
    updateMoney(parseInt(parseFloat(display.innerText) * 1000));
    display.innerText = '0';
  } else if (key === 'arrow') {
    updateMoney(2000000);
    display.innerText = '←';
  } else if (key === 'dot') {
    display.innerText += '.';
  } else if (key.startsWith('key')) {
    if (display.innerText === '0') {
      display.innerText = key[key.length - 1];
    } else {
      display.innerText += key[key.length - 1];
    }
  }
}

function updateMoney(money) {
  if (plus_player_id !== 0) {
    players_money[plus_player_id] += money;
    document.getElementById('display-plus').innerText = players_money[plus_player_id];
  }
  if (minus_player_id !== 0) {
    players_money[minus_player_id] -= money;
    document.getElementById('display-minus').innerText = players_money[minus_player_id];
  }
  console.log(players_money);
}
