    <script>
        var an = document.querySelector('.an');
        var text = document.querySelector('textarea');
        var main = document.querySelector('#left')
        an.onclick = function () {
            if (text.value == '') {
                alert('您没有输入内容');
                return false;
            }
            else {
                var commentnew = document.createElement('div');
                commentnew.setAttribute('class', 'comment');
                main.appendChild(commentnew);
                var img = document.createElement('img');
                img.setAttribute('src', '铁子.png');
                img.setAttribute('alt', '我');
                commentnew.appendChild(img);
                var a1 = document.createElement('a');
                a1.setAttribute('class', 'name');
                a1.setAttribute('href', 'https://baike.baidu.com/item/%E5%8F%B3%E7%94%B0%E5%8F%8C%E9%93%81/23414489?fromModule=lemma_inlink');
                a1.setAttribute('target', '_blank');
                a1.innerHTML = '我';
                commentnew.appendChild(a1);
                var say = document.querySelector('#say');
                var p1 = document.createElement('p');
                p1.innerHTML = say.value;
                commentnew.appendChild(p1);
                var span = document.querySelector('.clock')
                var span1 = document.createElement('span');
                span1.innerHTML = TIME;
                commentnew.appendChild(span1);
                var a2 = document.createElement('a');
                a2.setAttribute('class', 'good');
                a2.setAttribute('href', 'https://baike.baidu.com/item/%E7%88%B1%E4%B8%8A%E7%81%AB%E8%BD%A6/22553731#1_4');
                a2.setAttribute('target', '_blank');
                a2.innerHTML = '赞';
                commentnew.appendChild(a2);
                text.value = '';
            }

        }</script>
        <script>
                var clock = document.querySelector('.clock');
                var time = new Date();
                var timey = time.getFullYear();
                var timem = time.getMonth() + 1;
                var timeM = time.getDate();
                var TIME = timey + '/' + timem + '/' + timeM;
                clock.innerHTML = TIME;
        </script>
        <script>
        var btn = document.querySelector('.btn')
        var qr = document.querySelector('#qr')
        btn.onclick = function () {
            qr.style.display = 'none';
            btn.style.display = 'none';
        }
        </script>