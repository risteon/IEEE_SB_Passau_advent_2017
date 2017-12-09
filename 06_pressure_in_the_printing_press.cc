// -- BEGIN LICENSE BLOCK ----------------------------------------------
// -- END LICENSE BLOCK ------------------------------------------------
//----------------------------------------------------------------------
/*!\file
 *
 * \author  Christoph Rist <rist.christoph@gmail.com>
 * \date    2017-12-01
 *
 */
//----------------------------------------------------------------------

#include <algorithm>
#include <vector>
#include <memory>

#include <iostream>
#include <fstream>
#include <iomanip>


class Array2D
{
public:
  using T = char;
  using d_type = std::vector<T>;
  using ConstPtr = std::shared_ptr<const Array2D>;
  using Ptr = std::shared_ptr<Array2D>;

  friend class Array2DView;

  Array2D() = delete;
  explicit Array2D(uint32_t size_x, uint32_t size_y)
    : size_x_(size_x)
    , size_y_(size_y)
  {
    data_.resize(size_x * size_y);
  }
  explicit Array2D(std::istream& input)
  {
    input >> size_y_ >> size_x_;
    data_.resize(size_x_ * size_y_);
    input.ignore();
    for (uint32_t y = 0; y < size_y_; ++y)
    {
      input.read(data_.data() + y * size_x_, size_x_);
      input.ignore();
    }
  }

  uint32_t sizeX() const { return size_x_; }
  uint32_t sizeY() const { return size_y_; }

private:
  uint32_t size_x_;
  uint32_t size_y_;
  d_type data_;
};

class Array2DView
{
public:
  Array2DView() = delete;
  explicit Array2DView(Array2D::ConstPtr& arr)
          : arr_(arr)
          , size_x_(arr->sizeX())
          , size_y_(arr->sizeY())
          , pos_x_(0)
          , pos_y_(0)
  {}
  explicit Array2DView(Array2D::ConstPtr& arr,
              uint32_t size_x, uint32_t size_y,
              uint32_t pos_x, uint32_t pos_y)
    : arr_(arr)
    , size_x_(size_x)
    , size_y_(size_y)
    , pos_x_(pos_x)
    , pos_y_(pos_y)
  {}

  bool compareToTemplate(Array2DView& templ, char wildcard) const
  {
    if (size_x_ != templ.size_x_ || size_y_ != templ.size_y_)
      return false;

    for (uint32_t x = 0; x < size_x_; ++x)
    {
      for (uint32_t y = 0; y < size_y_; ++y)
      {
        const char t_at = templ.getAt(x, y);
        if (t_at == wildcard)
          continue;
        else if (t_at != getAt(x, y))
          return false;
      }
    }
    return true;
  }

  char getAt(uint32_t x, uint32_t y) const
  {
    return arr_->data_[(pos_y_ + y) * arr_->sizeX() + pos_x_ + x];
  }

private:
  Array2D::ConstPtr arr_;
  uint32_t size_x_;
  uint32_t size_y_;
  uint32_t pos_x_;
  uint32_t pos_y_;
};

//! The actual task
void work(std::istream &input, std::ostream &output)
{
  Array2D::ConstPtr card_template = std::make_shared<Array2D>(input);
  Array2D::ConstPtr sheet = std::make_shared<Array2D>(input);

  Array2DView card_template_view{card_template};

  // sanity check
  if (sheet->sizeX() % card_template->sizeX() || sheet->sizeY() % card_template->sizeY())
    throw std::runtime_error("wrong dimensions");

  uint32_t num_equals = 0;

  const uint32_t sheet_x = sheet->sizeX() / card_template->sizeX();
  const uint32_t sheet_y = sheet->sizeY() / card_template->sizeY();

  for (uint32_t x = 0; x < sheet_x; ++x)
  {
    for (uint32_t y = 0; y < sheet_y; ++y)
    {
      Array2DView view{sheet,
                             card_template->sizeX(),
                             card_template->sizeY(),
                             x * card_template->sizeX(),
                             y * card_template->sizeY()};
      if (view.compareToTemplate(card_template_view, '_'))
        ++num_equals;
    }
  }

  output << num_equals << std::endl;
}


int main(int argc, char** argv)
{
  //! if arguments are specified, treat them as files to read from/write to
  std::ifstream f_in{};
  std::ofstream f_out{};
  if (argc <= 1)
  {
    work(std::cin, std::cout);
  }
  else if (argc > 2)
  {
    f_out.open(argv[2]);
    if (!f_out.good())
      return 1;
    work(f_in, f_out);
  }
  else
  {
    f_in.open(argv[1]);
    if (!f_in.good())
      return 1;
    work(f_in, std::cout);
  }
  return 0;
}
