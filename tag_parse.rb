class Stack
  def initialize
    @stack = Array.new()
  end

  def push(item)
    @stack.push(item)
  end

  def pop
    @stack.pop
  end

  def look
    @stack.last
  end

  def isEmpty
    @stack == []
  end

  def length
    @stack.length
  end

  def peek
    @stack[-1]
  end
end

def html_filtrele(file)
  list = []

  myfile = File.open(file)
  myfile.each do |line|
    i = 0

    while i <= line.length do
      if line[i] == "<"
        container = ""
        i = i + 1

        while line[i] != ">"
          container = container + line[i]
          i = i + 1
        end

        list.push(container)
        container = ""
      end
      i = i + 1
    end
  end
  return list
end


def tag_checker(tag_list)
  opens = ["html","body","head","p","li","dir","div","ul","form","h1"]      #TODO diger taglari ekle
  balance = true
  i = 0
  stack = Stack.new()

  while i < tag_list.length and balance
    tag = tag_list[i]

    if opens.include? tag
      stack.push(tag)
    else
      if stack.isEmpty()
        balance = false
      else
        top = stack.pop()
        if not matches(top,tag)
          balance = false
        end
      end
    end
    i = i + 1
  end
  if balance and stack.isEmpty()
    return true
  else
    return false
  end
end

def matches(open,close)
  opens = ["html","body","head","p","li","dil","div","ul","form","h1"]
  closers = ["/html","/body","/head","/p","/li","/dil","/div","/ul","/form","h1"]
  return opens.index(open) == closers.index(close)
end

def html_tag_checker(html_page)
  liste = html_filtrele(html_page)
  return tag_checker(liste)
end

puts html_tag_checker("true_text.html")    #check edilecek htlm dosyasini argman olarak alir.
